# gradio_app.py
import gradio as gr
from frontend.input_handlers import InputHandlers
from config import Config

def create_gradio_interface():
    """Create and configure the Gradio web interface.
    
    Returns:
        gradio.Blocks: The configured Gradio interface
    """
    with gr.Blocks(title="Jewelry Recommender") as demo:
        gr.Markdown("# Jewelry Recommendation System")
        gr.Markdown("Upload an image of jewelry to get similar recommendations.")
        
        with gr.Tab("Upload Image"):
            with gr.Row():
                image_input = gr.Image(type="pil", label="Upload Jewelry Image")
                num_recs_slider = gr.Slider(
                    minimum=1, 
                    maximum=Config.MAX_RECOMMENDATIONS, 
                    value=Config.DEFAULT_NUM_RECOMMENDATIONS, 
                    step=1, 
                    label="Number of Recommendations"
                )
            skip_exact = gr.Checkbox(value=True, label="Skip Exact Match")
            submit_btn = gr.Button("Get Recommendations")
            output_html = gr.HTML(label="Recommendations")
            submit_btn.click(
                InputHandlers.process_image, 
                inputs=[image_input, num_recs_slider, skip_exact], 
                outputs=output_html
            )
        
        with gr.Tab("Image URL"):
            with gr.Row():
                url_input = gr.Textbox(label="Enter Image URL")
                url_num_recs = gr.Slider(
                    minimum=1, 
                    maximum=Config.MAX_RECOMMENDATIONS, 
                    value=Config.DEFAULT_NUM_RECOMMENDATIONS, 
                    step=1, 
                    label="Number of Recommendations"
                )
            url_skip_exact = gr.Checkbox(value=True, label="Skip Exact Match")
            url_btn = gr.Button("Get Recommendations from URL")
            url_output = gr.HTML(label="Recommendations")
            url_btn.click(
                InputHandlers.process_url, 
                inputs=[url_input, url_num_recs, url_skip_exact], 
                outputs=url_output
            )
        
        with gr.Tab("Base64 Image"):
            with gr.Row():
                base64_input = gr.Textbox(label="Enter Base64 Image String")
                base64_num_recs = gr.Slider(
                    minimum=1, 
                    maximum=Config.MAX_RECOMMENDATIONS, 
                    value=Config.DEFAULT_NUM_RECOMMENDATIONS, 
                    step=1, 
                    label="Number of Recommendations"
                )
            base64_skip_exact = gr.Checkbox(value=True, label="Skip Exact Match")
            base64_btn = gr.Button("Get Recommendations from Base64")
            base64_output = gr.HTML(label="Recommendations")
            base64_btn.click(
                InputHandlers.process_base64, 
                inputs=[base64_input, base64_num_recs, base64_skip_exact], 
                outputs=base64_output
            )
        
        gr.Markdown("## How to Use")
        gr.Markdown("""
        1. Upload an image of jewelry, provide an image URL, or paste a base64-encoded image
        2. Adjust the number of recommendations you want to see
        3. Check "Skip Exact Match" to exclude the identical or closest match from results
        4. Click the 'Get Recommendations' button
        5. View similar jewelry items based on visual similarity
        """)
        
    return demo
