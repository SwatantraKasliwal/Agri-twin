export function getNextStep() {
  return {
    soil_moisture: 62,
    heat_stress: 28,
    rainfall: 10,
    crop_stage: "Vegetative",
    irrigation_mm: 18.2,
    explanation: [
      "Soil moisture is moderate",
      "Heat stress is increasing",
      "Rainfall contribution is low",
      "Crop is in a sensitive growth stage",
    ],
  };
}

