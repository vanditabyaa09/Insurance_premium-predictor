from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse (BaseModel) :
    predicted_category : str = Field(
        ..., 
        description="The Predicted Premium Insurance Category",
        example = "High"
    )

    confidence : float = Field(
        ..., 
        description="Models confidence Score fo the predicted Class",
        example = "0.45"
    ) 

    class_probabilities : Dict[str, float] = Field(
        ...,
        description="Probability distributuion across all possible classes",
        example = {"Low" : 0.1, "Medium" : 0.15, "High" : 0.84}
    )