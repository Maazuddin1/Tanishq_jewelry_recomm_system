# formatter.py

class ResultFormatter:
    """Formats recommendation results for display."""
    
    @staticmethod
    def format_html(recommendations):
        if not recommendations:
            print("No recommendations found.")  # Debug log
            return "No recommendations found."
    
        result_html = "<h3>Recommended Jewelry Items:</h3>"
        for i, rec in enumerate(recommendations, 1):
            metadata = rec["metadata"]
            result_html += f"<div style='margin-bottom:15px; padding:10px; border:1px solid #ddd; border-radius:5px;'>"
            result_html += f"<h4>#{i}: {metadata.get('name', 'Unknown')}</h4>"
            result_html += f"<p><b>Category:</b> {metadata.get('category', 'Unknown')}</p>"
            result_html += f"<p><b>Description:</b> {metadata.get('description', 'No description available')}</p>"
            result_html += f"<p><b>Price:</b> ${metadata.get('price', 'N/A')}</p>"
            result_html += f"<p><b>Similarity Score:</b> {rec['similarity_score']:.4f}</p>"
            if 'image_url' in metadata:
                result_html += f"<p><img src='{metadata['image_url']}' style='max-width:200px; max-height:200px;'></p>"
            result_html += "</div>"
    
        print("HTML output generated:", result_html)  # Debug log
        return result_html    
    @staticmethod
    def format_json(recommendations):
        """Format recommendations as JSON.
        
        Args:
            recommendations (list): List of recommendation dictionaries
            
        Returns:
            list: Clean JSON-serializable results
        """
        if not recommendations:
            return []
        
        results = []
        for rec in recommendations:
            results.append({
                "item": rec["metadata"].get("name", "Unknown"),
                "category": rec["metadata"].get("category", "Unknown"),
                "description": rec["metadata"].get("description", "No description"),
                "price": rec["metadata"].get("price", "N/A"),
                "similarity_score": round(rec["similarity_score"], 4),
                "image_url": rec["metadata"].get("image_url", None)
            })
        
        return results
