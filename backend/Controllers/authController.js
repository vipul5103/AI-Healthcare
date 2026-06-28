import User from "../models/UserSchema.js";
import Doctor from "../models/DoctorSchema.js";
import jwt from "jsonwebtoken";
import bcrypt from "bcryptjs";

// Generate JWT Token
const generateToken = (user) => {
  if (!process.env.JWT_SECRET_KEY) {
    throw new Error("JWT secret key is not defined in environment variables");
  }

  return jwt.sign(
    { id: user._id, role: user.role }, // Payload: user ID and role
    process.env.JWT_SECRET_KEY, // Secret key from .env
    { expiresIn: "15d" } // Token expiry
  );
};

// Register function (for user sign-up)
export const register = async (req, res) => {
  const { email, password, name, role, photo, gender } = req.body;

  try {
    let user = null;

    if (role === "patient") {
      user = await User.findOne({ email });
    } else if (role === "doctor") {
      user = await Doctor.findOne({ email });
    }

    // Check if user exists
    if (user) {
      return res.status(400).json({ message: "User already exists" });
    }

    // Hash password
    const salt = await bcrypt.genSalt(10);
    const hashPassword = await bcrypt.hash(password, salt);

    // Create new user based on role (patient or doctor)
    if (role === "patient") {
      user = new User({
        name,
        email,
        password: hashPassword,
        photo,
        gender,
        role,
      });
    }

    if (role === "doctor") {
      user = new Doctor({
        name,
        email,
        password: hashPassword,
        photo,
        gender,
        role,
      });
    }

    // Save user to the database
    await user.save();

    // Dynamically generate token after signup
    const token = generateToken(user);

    // Return success message along with token
    res.status(200).json({
      success: true,
      message: "User successfully created",
      token, // Send token in response
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Internal server error, Try again",
    });
  }
};

// Login function (for user login)
export const login = async (req, res) => {
  const { email, password } = req.body;

  try {
    let user = null;

    const patient = await User.findOne({ email });
    const doctor = await Doctor.findOne({ email });
    const admin = await User.findOne({ email, role: "admin" }); // Add admin check

    if (patient) {
      user = patient;
    }
    if (doctor) {
      user = doctor;
    }
    if (admin) {
      user = admin; // Handle admin login
    }

    // Check if user exists
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    // Compare password
    const isPasswordMatch = await bcrypt.compare(password, user.password);

    if (!isPasswordMatch) {
      return res.status(401).json({
        status: false,
        message: "Invalid Credentials, try again",
      });
    }

    // Dynamically generate token after login
    const token = generateToken(user);

    // Send token in response
    const { password: userPassword, role, appointments, ...rest } = user._doc;
    res.status(200).json({
      status: true,
      message: "Successfully logged in",
      token, // Send token in response
      data: { ...rest },
      role,
    });
  } catch (error) {
    console.error("Error during login:", error);
    res.status(500).json({
      status: false,
      message: "Failed to login due to an internal error",
    });
  }
};
