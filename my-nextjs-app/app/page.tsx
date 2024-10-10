"use client"; // Add this to make the component a Client Component

import React, { useState } from "react";

export default function Home() {
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [recognizedText, setRecognizedText] = useState<string | null>(null); // State for recognized text

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const imageUrl = URL.createObjectURL(file);
      setImagePreview(imageUrl);
    } else {
      setImagePreview(null);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const imageElement = document.getElementById("image") as HTMLInputElement;

    if (!imageElement || !imageElement.files) {
      console.error("Form elements or image files not found");
      return;
    }

    const formData = new FormData();
    formData.append("image", imageElement.files[0]);

    try {
      const res = await fetch("http://localhost:8000/ocrapi", {
        method: "POST",
        body: formData,
      });

      if (res.ok) {
        const data = await res.json();
        setRecognizedText(data.recognized_text); // Set the recognized text in state
        console.log("Data submitted successfully");
      } else {
        console.error("Failed to submit data");
      }
    } catch (error) {
      console.error("Error submitting data", error);
    }
  };

  return (
    <div>
      <form onChange={handleSubmit}>
        <label>
          Image:
          <input
            type="file"
            id="image"
            name="image"
            accept="image/*"
            required
            onChange={handleImageChange}
          />
        </label>
      </form>

      {/* Show image preview if available */}
      {imagePreview && (
        <div>
          <img src={imagePreview} alt="Selected" style={{ maxWidth: "500px" }} />
        </div>
      )}

      {/* Show recognized text if available */}
      {recognizedText !== null ? (
        <div>
          <h3>Recognized Text:</h3>
          <p>{recognizedText}</p>
        </div>
      ) : (
        <p>Recognized text will be shown here</p>
      )}

    </div>
  );
}
