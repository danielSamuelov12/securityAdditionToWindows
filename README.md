
---

# Advanced Security System with Face ID and User Image Capture

## Overview
This security system adds an extra layer of protection to your computer by capturing an image of the user whenever they log into their account. The system works alongside the existing password security and uses Face ID technology to authenticate users. If someone tries to log into the account, the system takes a photo and saves it in an encrypted folder for future reference. This can help identify who accessed your account.

If the Face ID authentication fails, the system will shut down the computer, preventing unauthorized access.

## Features
- **Face Recognition**: Uses Face ID to authenticate users.
- **Image Capture**: Automatically takes a picture of the user during login attempts.
- **Encrypted Image Storage**: The captured image is stored in a secure, encrypted folder to protect privacy.
- **Automatic Startup**: The security system starts automatically when the computer is turned on.
- **Face ID Creation**: A separate script, `faceIdCreation.py`, is used to create a Face ID image. This image is used for authentication purposes. It is recommended to run this script once to set up the face recognition.
- **Shutdown on Failure**: If the Face ID authentication fails, the system will shut down the computer, preventing an unauthorized person from accessing the account.

## Installation Instructions
1. Clone the repository to your local machine or download the zip file.
2. Ensure you have all the necessary dependencies installed, such as Face ID authentication software.
3. Run the `faceIdCreation.py` script once to create the Face ID image. This image will be used for authentication.
4. Add the `securitySystem.vbs` file to the `shell:startup` folder to ensure the system runs automatically on startup. You can do this by:
   - Press `Win + R` and type `shell:startup`, then press Enter.
   - Place the `securitySystem.vbs` file in the folder that opens.
5. Modify the system settings to meet your specific requirements (such as face recognition setup).

## Usage
- Once the system is installed and running, it will prompt you for Face ID authentication upon login.
- If a login attempt is successful, the system captures an image of the user and stores it in an encrypted folder.
- If the Face ID authentication fails, the system will shut down the computer to prevent unauthorized access.
- You can view the captured images by decrypting the folder with the appropriate password or key.

## Security Notes
- Ensure that your Face ID and image storage are configured securely.
- Only authorized personnel should have access to the encrypted photo folder.

## License
This project is licensed under the MIT License.

## Copyright
© 2025 Daniel Samuelov. All rights reserved.

---

