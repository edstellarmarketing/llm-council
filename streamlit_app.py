import streamlit as st
import os
import re
from openai import OpenAI

# Page config
st.set_page_config(page_title="LLM Council - Edstellar", page_icon="🏛️", layout="wide")

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# Council members configuration
COUNCIL_MEMBERS = [
    {"name": "Claude", "model": "anthropic/claude-3.5-sonnet", "color": "#4CAF50"},
    {"name": "GPT-4", "model": "openai/gpt-4-turbo", "color": "#F44336"},
    {"name": "Gemini", "model": "google/gemini-flash-1.5", "color": "#2196F3"},
    {"name": "Grok", "model": "x-ai/grok-2-1212", "color": "#9C27B0"},
]

# Edstellar Sales Email Rules
EDSTELLAR_RULES = """# Edstellar Sales Email Rules Guide

## Core Principles
- Professional, conversational tone balancing warmth with authority
- Clear value proposition without aggressive sales language
- Respectful of recipient's time and decision-making process
- Focus on partnership and long-term relationship building

## Email Structure

### Subject Lines
- Keep under 60 characters
- Action-oriented and specific
- Include company name or key benefit
- Avoid spam triggers (FREE, !!!, URGENT)
- Examples:
  * "Customized [Topic] Training for [Company]"
  * "Addressing [Company]'s [Specific Need]"
  * "Partnership Opportunity: [Value Proposition]"

### Opening (First 2 sentences)
- Personalize with recipient's name and title
- Reference specific context (mutual connection, recent event, company news)
- State clear purpose immediately
- Example: "Dear [Name], I noticed [Company] recently [specific observation]. I'm reaching out to explore how Edstellar can support your team's development in [specific area]."

### Body Content

#### Value Proposition (2-3 sentences)
- Lead with client benefit, not company features
- Use specific, quantifiable outcomes when possible
- Connect to recipient's likely pain points
- Avoid generic claims ("world-class", "best-in-class")

#### Credibility Markers (1-2 sentences)
- Mention relevant experience (14 years, Fortune 500 clients)
- Reference similar industry clients (without naming unless public)
- Cite specific expertise relevant to their need
- Keep brief - this is support, not the main message

#### Call to Action
- Single, clear next step
- Low-commitment ask (15-min call, brief conversation)
- Provide specific time options when possible
- Make it easy to say yes
- Examples:
  * "Would you be open to a brief 15-minute call next week?"
  * "I'd love to share some specific examples - do you have 20 minutes this Thursday or Friday?"

### Closing
- Professional sign-off: "Best regards," or "Warm regards,"
- Full name and title
- Contact information
- Optional: One-line value reminder

## Language Guidelines

### Do Use:
- "Explore", "discuss", "share insights"
- "Customized", "tailored", "specific to your needs"
- "Support", "partnership", "collaboration"
- "Challenge", "opportunity", "goal"
- Active voice and strong verbs
- Industry-specific terminology (when appropriate)

### Avoid:
- "Revolutionize", "transform", "disrupt"
- "Just checking in", "following up"
- "Opportunity of a lifetime", "limited time"
- Multiple exclamation points
- Jargon without context
- Passive voice
- Apologetic language ("Sorry to bother you")

## Tone Calibration

### For C-Suite/Senior Leaders:
- More concise (under 150 words)
- Strategic focus (ROI, competitive advantage)
- Acknowledge their time constraints
- Reference business outcomes over features

### For HR/L&D Professionals:
- Can be slightly longer (150-200 words)
- Focus on implementation ease and learner outcomes
- Emphasize customization and support
- Mention metrics and reporting

### For Technical Managers:
- Highlight technical depth and instructor expertise
- Mention specific technologies and methodologies
- Focus on practical application
- Reference hands-on components

## Follow-up Guidelines

### First Follow-up (3-4 business days):
- Reference original email briefly
- Add new value (case study, resource, insight)
- Restate CTA more directly
- Keep even shorter than original

### Second Follow-up (1 week later):
- Acknowledge multiple touchpoints professionally
- Offer alternative (different service, resource, or simply to connect later)
- Include easy "opt-out" language
- Final attempt should feel helpful, not pushy

### Maximum Touch Points:
- Initial email + 2 follow-ups = 3 total
- After 3 attempts, wait 3-6 months unless they engage
- Always respect explicit "not interested" responses

## Personalization Requirements

### Minimum for Every Email:
- Recipient's correct name and title
- Company name
- One specific observation about their company/role/industry
- Relevant service offering (not generic)

### Advanced Personalization (When Possible):
- Reference to recent company news or initiatives
- Mention of mutual connection
- Industry-specific pain point or trend
- Previous interaction or engagement

## Quality Checklist Before Sending

- [ ] Subject line under 60 characters and compelling
- [ ] Recipient name and title verified and correct
- [ ] At least one personalized element specific to recipient
- [ ] Clear value proposition in first paragraph
- [ ] Single, specific call to action
- [ ] Professional but warm tone throughout
- [ ] No spelling or grammatical errors
- [ ] All links working (if included)
- [ ] Mobile-friendly formatting (short paragraphs)
- [ ] Under 200 words total

## Red Flags to Avoid
- Generic greetings ("Dear Sir/Madam")
- No clear purpose by second sentence
- Multiple CTAs or confusing next steps
- Overly long paragraphs (>3 sentences)
- Excessive use of "I/we" vs "you/your"
- Spelling recipient's name or company wrong
- Attachment without context (avoid attachments in cold emails)
- Requesting too much time (>30 minutes) initially

## Context-Specific Adaptations

### For Course Page Inquiries:
- Reference the specific course they viewed
- Mention customization options
- Offer to discuss their specific needs
- Include brief overview of what customization includes

### For General Training Needs:
- Ask qualifying questions
- Offer needs assessment
- Suggest initial consultation
- Avoid premature solutions

### For Specific Event/Workshop Requests:
- Confirm understanding of requirements
- Outline high-level approach
- Mention relevant past successes
- Provide clear next steps for proposal

## Response Handling

### If They Reply Positively:
- Respond within 4 business hours
- Express appreciation briefly
- Confirm next steps clearly
- Provide calendar link or specific times

### If They Ask for More Information:
- Provide requested info concisely
- Add one additional relevant resource
- Restate clear next step
- Make it easy to schedule conversation

### If They Decline:
- Thank them professionally
- Ask if timing is the issue
- Offer to stay in touch for future
- Request referral if appropriate

## Edstellar-Specific Talking Points

### Key Differentiators:
- 14 years of corporate training experience
- 5,000+ expert trainers globally
- Presence in 100+ locations
- Fortune 500 client experience
- Customization expertise
- On-site and virtual delivery options

### When to Mention What:
- First email: 1-2 differentiators max, relevant to their need
- Follow-up: Different angle or deeper detail
- Never list all differentiators - overwhelms and dilutes

### Customization Messaging:
- "Tailored to your specific business context"
- "Designed around your team's current skill levels and goals"
- "Incorporates your real-world scenarios and challenges"
- Avoid: "Fully customizable" (vague and overused)"""

def parse_enquiry(enquiry_text):
    """Parse the enquiry text to extract key information"""
    info = {
        "name": "",
        "email": "",
        "organization": "",
        "job_title": "",
        "country": "",
        "phone": "",
        "training_needs": "",
        "page": "",
        "origin": ""
    }
    
    # Extract information using regex
    patterns = {
        "name": r"Name\s*-\s*(.+?)(?:\n|$)",
        "email": r"Email\s*-\s*(.+?)(?:\n|$)",
        "organization": r"Organization Name\s*-\s*(.+?)(?:\n|$)",
        "job_title": r"Job Title\s*-\s*(.+?)(?:\n|$)",
        "country": r"Country\s*-\s*(.+?)(?:\n|$)",
        "phone": r"Phone Number\s*-\s*(.+?)(?:\n|$)",
        "training_needs": r"Training Needs\s*-\s*(.+?)(?:\n|$)",
        "page": r"Page\s*-\s*(.+?)(?:\n|$)",
        "origin": r"Origin\s*-\s*(.+?)(?:\n|$)"
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, enquiry_text, re.IGNORECASE)
        if match:
            info[key] = match.group(1).strip()
    
    return info

def get_council_response(enquiry_info, member, rules):
    """Get response from a council member with rules"""
    system_prompts = {
        "Claude": f"You are an expert email advisor using Claude AI. Generate professional, nuanced sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
        "GPT-4": f"You are an expert email advisor using GPT-4. Generate clear, effective sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
        "Gemini": f"You are an expert email advisor using Google Gemini. Generate comprehensive, well-structured sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
        "Grok": f"You are an expert email advisor using Grok AI. Generate engaging, creative sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
    }
    
    context = f"""
    Recipient Name: {enquiry_info['name']}
    Job Title: {enquiry_info['job_title']}
    Organization: {enquiry_info['organization']}
    Email: {enquiry_info['email']}
    Country: {enquiry_info['country']}
    Phone: {enquiry_info['phone']}
    Training Needs: {enquiry_info['training_needs']}
    Source Page: {enquiry_info['page']}
    Origin/Course: {enquiry_info['origin']}
    """
    
    try:
        response = client.chat.completions.create(
            model=member["model"],
            messages=[
                {"role": "system", "content": system_prompts[member["name"]]},
                {"role": "user", "content": f"Generate a complete sales email based on this enquiry information:\n\n{context}"}
            ],
            max_tokens=800,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# UI
st.title("🏛️ Edstellar Sales Email Generator")
st.markdown("Generate professional sales emails following Edstellar's best practices")

# Sidebar for rules
with st.sidebar:
    st.header("📋 Email Writing Rules")
    st.markdown("**Edstellar Sales Email Guidelines**")
    
    with st.expander("View Complete Rules Guide"):
        st.markdown(EDSTELLAR_RULES)
    
    use_custom = st.checkbox("Use custom rules instead", value=False)
    
    if use_custom:
        rules = st.text_area(
            "Enter your custom rules:",
            value=EDSTELLAR_RULES,
            height=300,
            help="Modify the rules as needed"
        )
    else:
        rules = EDSTELLAR_RULES

# Main content
st.markdown("### Paste Enquiry Details")

enquiry_text = st.text_area(
    "Paste the complete enquiry email here:",
    height=300,
    placeholder="""From: <business@edstellar.com>
Date: Fri, Nov 28, 2025 at 12:49 PM
Subject: Edstellar Enquiry - course page
To: <business@edstellar.com>

Hello Edstellar Admin,

You have received an enquiry from Anoop Singh Dangi. The organisation details are furnished below -      

      Name - Anoop Singh Dangi
      Email - sm36968@gmail.com
      Organization Name - REC Limited
      Job Title - Officer
      Country - India (भारत)
      Country Code - 91
      Phone Number - 9474259390          
      Training Needs - Oracle EBS r12 Technical and DBA training required at on-site.
      Page - course 
      Origin - oracle-database-19c-administration-training""",
    help="Paste the entire enquiry email from Edstellar"
)

if st.button("Generate Email Variations", type="primary"):
    if enquiry_text.strip():
        # Parse the enquiry
        enquiry_info = parse_enquiry(enquiry_text)
        
        # Display parsed information
        with st.expander("📊 Parsed Information", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Name:** {enquiry_info['name']}")
                st.write(f"**Organization:** {enquiry_info['organization']}")
                st.write(f"**Job Title:** {enquiry_info['job_title']}")
                st.write(f"**Email:** {enquiry_info['email']}")
            with col2:
                st.write(f"**Country:** {enquiry_info['country']}")
                st.write(f"**Phone:** {enquiry_info['phone']}")
                st.write(f"**Page:** {enquiry_info['page']}")
                st.write(f"**Origin:** {enquiry_info['origin']}")
            st.write(f"**Training Needs:** {enquiry_info['training_needs']}")
        
        # Generate emails
        with st.spinner("Generating email variations from different AI models..."):
            cols = st.columns(2)
            
            for idx, member in enumerate(COUNCIL_MEMBERS):
                with cols[idx % 2]:
                    st.markdown(f"### {member['name']}")
                    response = get_council_response(enquiry_info, member, rules)
                    
                    # Display the email
                    st.markdown(
                        f"<div style='background-color: {member['color']}22; padding: 20px; border-radius: 10px; border-left: 4px solid {member['color']};'>{response}</div>",
                        unsafe_allow_html=True
                    )
                    
                    # Copy button
                    with st.expander(f"📋 Copy {member['name']}'s Email"):
                        st.code(response, language=None)
                    
                    st.markdown("---")
    else:
        st.warning("Please paste an enquiry email first!")

# Footer
st.markdown("---")
st.markdown("💡 **Tips:**")
st.markdown("- Simply paste the entire enquiry email - the system will automatically extract relevant information")
st.markdown("- Review all four AI-generated variations to find the best tone and approach")
st.markdown("- Always customize the generated email with specific details before sending")
