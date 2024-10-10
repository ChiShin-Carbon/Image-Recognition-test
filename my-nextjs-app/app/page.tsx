"use client"; // Add this to make the component a Client Component

import React from "react";

export default function Home() {
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // Prevent the default form submission behavior

    // Get input elements
    const nameElement = document.getElementById("name") as HTMLInputElement;
    const ageElement = document.getElementById("age") as HTMLInputElement;

    if (!nameElement || !ageElement) {
      console.error("Form elements not found");
      return;
    }

    // Prepare the data to send
    const data = {
      name: nameElement.value,
      age: ageElement.value,
    };

    try {
      // Send a POST request to the backend
      const res = await fetch("http://localhost:8000/create-test", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (res.ok) {
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
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" id="name" name="name" required />
        </label>
        <label>
          Age:
          <input type="text" id="age" name="age" required />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
