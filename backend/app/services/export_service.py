"""
Export service - Generate PDF reports
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
from pathlib import Path
from app.config import settings
from app.api.dependencies import ModelDependencies

class ExportService:
    """Handle PDF export operations"""
    
    def create_report(self, doc_id: str, doc: dict, request, models: ModelDependencies) -> str:
        """Generate PDF report"""
        
        output_path = Path(settings.EXPORT_DIR) / f"{doc_id}_report.pdf"
        pdf_doc = SimpleDocTemplate(str(output_path), pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#4C1D95'),
            spaceAfter=30
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#7C3AED'),
            spaceAfter=12
        )
        
        # Title
        story.append(Paragraph("Financial Report Analysis", title_style))
        story.append(Paragraph(f"Document: {doc['filename']}", styles['Normal']))
        story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Summary
        if request.include_summary and doc.get('summary'):
            story.append(Paragraph("Executive Summary", heading_style))
            summary = doc['summary']
            
            summary_data = [
                ['Metric', 'Value'],
                ['Revenue', summary.get('revenue', 'N/A')],
                ['Net Profit', summary.get('profit', 'N/A')],
                ['Profit Margin', summary.get('profitMargin', 'N/A')],
                ['EPS', summary.get('eps', 'N/A')]
            ]
            
            t = Table(summary_data, colWidths=[2.5*inch, 3*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7C3AED')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(t)
            story.append(Spacer(1, 0.2*inch))
            
            # Risks
            story.append(Paragraph("Key Risks", heading_style))
            for i, risk in enumerate(summary.get('key_risks', [])[:5], 1):
                story.append(Paragraph(f"{i}. {risk}", styles['Normal']))
            story.append(Spacer(1, 0.2*inch))
        
        # Sentiment
        if request.include_sentiment and doc.get('sentiment'):
            story.append(Paragraph("Sentiment Analysis", heading_style))
            sentiment = doc['sentiment']
            
            sentiment_data = [
                ['Category', 'Percentage'],
                ['Positive', f"{sentiment['breakdown']['positive']}%"],
                ['Neutral', f"{sentiment['breakdown']['neutral']}%"],
                ['Negative', f"{sentiment['breakdown']['negative']}%"]
            ]
            
            t = Table(sentiment_data, colWidths=[2.5*inch, 2*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7C3AED')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(t)
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph(
                f"Overall: <b>{sentiment['overall'].upper()}</b> (Score: {sentiment['score']:.2f})", 
                styles['Normal']
            ))
        
        pdf_doc.build(story)
        return str(output_path)