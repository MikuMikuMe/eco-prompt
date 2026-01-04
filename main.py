Below is a complete Python program for the Eco-Prompt project. This application uses a simulated natural language processing (NLP) model to generate context-aware prompts for eco-friendly practices. In a real-world scenario, you might replace the simulated model with a more sophisticated NLP library like Hugging Face's `transformers`. Here, we focus on structuring the program, handling errors, and providing comprehensive comments.

```python
import random

# Mock function to simulate NLP-based context-aware prompt generation
def generate_eco_prompt(context):
    """
    Generate an eco-friendly prompt based on the provided context.
    
    Args:
    context (str): The situation or context from which to generate a prompt.
    
    Returns:
    str: A prompt encouraging an eco-friendly action.
    """
    try:
        # A dictionary simulating different context-to-prompt mappings
        prompts = {
            "transport": [
                "Consider carpooling or using public transport to reduce carbon emissions.",
                "Could you bike or walk to your destination to help reduce air pollution?"
            ],
            "electricity": [
                "Remember to turn off lights when leaving a room to save energy.",
                "Unplug devices when not in use to conserve electricity."
            ],
            "waste": [
                "Try using a reusable bag instead of plastic bags while shopping.",
                "Consider starting a compost bin to reduce kitchen waste."
            ],
            "water": [
                "Turn off the tap while brushing your teeth to save water.",
                "Consider taking shorter showers to conserve water."
            ]
        }
        
        # Fetch a random prompt based on the context
        if context in prompts:
            prompt = random.choice(prompts[context])
        else:
            raise ValueError("Context not recognized. Please use a valid context such as 'transport', 'electricity', 'waste', or 'water'.")
        
        return prompt
    
    except Exception as e:
        return f"Error generating prompt: {str(e)}"

def eco_prompt_application():
    """
    Main application loop to interact with the user and display eco-friendly prompts.
    """
    print("Welcome to Eco-Prompt, your assistant for sustainable living!\n")
    
    # Provide instructions
    print("Please enter a context from the following for an eco-friendly prompt:")
    print("1. transport")
    print("2. electricity")
    print("3. waste")
    print("4. water\n")
    
    while True:
        try:
            # Get user's context choice
            user_input = input("Enter a context (or type 'exit' to quit): ").strip().lower()
            
            if user_input == 'exit':
                print("Thank you for using Eco-Prompt. Goodbye!")
                break
            
            # Generate and display the eco-prompt
            eco_prompt = generate_eco_prompt(user_input)
            print(f"\nEco-friendly Prompt:\n{eco_prompt}\n")
        
        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting the application.")
            break
        
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    eco_prompt_application()
```

### Explanation:
- **Eco-Friendly Prompts**: The program generates random eco-friendly prompts based on the user-provided context. It supports four contexts: transport, electricity, waste, and water.
- **Error Handling**: Uses error handling to provide feedback for incorrect contexts and other exceptions. It includes specific exceptions such as `ValueError` and catches all other exceptions.
- **User Interaction**: The application uses a command-line interface, allowing users to input contexts and receive suggestions. It gracefully exits when the user types "exit" or interrupts the program.

This program can be expanded by integrating a real NLP model and enriching the variety of contexts and prompts.