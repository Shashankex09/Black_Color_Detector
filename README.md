# Black Color Detector

A real-time computer vision application for detecting black colors in video streams using OpenCV and advanced image processing techniques.

## 🎯 Features

- **Real-time Detection**: Live video processing from webcam
- **Color Thresholding**: Advanced HSV color space filtering
- **Contour Detection**: Identify and highlight black objects
- **Morphological Operations**: Noise reduction and shape refinement
- **Performance Optimized**: Efficient frame processing

## 📋 Requirements

- Python 3.8+
- Webcam or video input device
- OpenCV-compatible camera drivers

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shashankex09/Black_Color_Detector.git
   cd Black_Color_Detector
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the black color detection:
```bash
python src/black_color_detection.py
```

The application will:
- Open your default webcam
- Process frames in real-time
- Display original video and black color mask
- Show detected contours

## 📁 Project Structure

```
Black_Color_Detector/
├── src/
│   └── black_color_detection.py    # Main detection script
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── .gitignore                     # Git ignore rules
```

## 🔧 Configuration

The script includes optimized settings for black color detection:

- **HSV Range**: Fine-tuned for black color detection
- **Morphological Operations**: Erosion and dilation for noise reduction
- **Contour Filtering**: Minimum area threshold for valid detections

## 🎨 How It Works

1. **Color Space Conversion**: RGB to HSV for better color segmentation
2. **Thresholding**: Apply black color range filtering
3. **Noise Reduction**: Morphological operations to clean the mask
4. **Contour Detection**: Find and draw contours around black objects
5. **Real-time Display**: Show processed results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit your changes (`git commit -m 'Add enhancement'`)
4. Push to the branch (`git push origin feature/enhancement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenCV](https://opencv.org/) for computer vision framework
- [NumPy](https://numpy.org/) for numerical computing

## 📞 Support

For questions or improvements, please open an issue on GitHub.

---

**Perfect for computer vision learning and black object detection applications**