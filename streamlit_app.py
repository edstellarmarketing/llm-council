import streamlit as st
import os
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
    {"name": "Gemini", "model": "google/gemini-pro-1.5", "color": "#2196F3"},
    {"name": "Grok", "model": "x-ai/grok-beta", "color": "#9C27B0"},
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

def get_council_response(question, member, rules):
    """Get response from a council member with rules"""
    system_prompts = {
        "Claude": f"You are an expert email advisor using Claude AI. Generate professional, nuanced sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
        "GPT-4": f"You are an expert email advisor using GPT-4. Generate clear, effective sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
        "Gemini": f"You are an expert email advisor using Google Gemini. Generate comprehensive, well-structured sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
        "Grok": f"You are an expert email advisor using Grok AI. Generate engaging, creative sales emails for Edstellar while strictly following the email rules. Generate a complete, professional email ready to send.\n\n{rules}",
    }
    
    try:
        response = client.chat.completions.create(
            model=member["model"],
            messages=[
                {"role": "system", "content": system_prompts[member["name"]]},
                {"role": "user", "content": f"Generate a complete sales email based on this context:\n\n{question}"}
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
st.markdown("### Email Context")

col1, col2 = st.columns(2)

with col1:
    recipient_name = st.text_input("Recipient Name", placeholder="e.g., Mr. Anoop Singh Dangi")
    company_name = st.text_input("Company Name", placeholder="e.g., REC Limited")

with col2:
    training_need = st.text_input("Training Topic", placeholder="e.g., Oracle EBS R12 Technical and DBA")
    origin = st.text_input("Source/Origin", placeholder="e.g., oracle-database-19c-administration-training")

additional_context = st.text_area(
    "Additional Context (optional):",
    height=100,
    placeholder="Any specific details about the inquiry, company news, or personalization points..."
)

# Construct the question
question = f"""
Recipient: {recipient_name}
Company: {company_name}
Training Need: {training_need}
Source: {origin}
Additional Context: {additional_context}
"""

if st.button("Generate Email Variations", type="primary"):
    if recipient_name and company_name and training_need:
        with st.spinner("Generating email variations..."):
            cols = st.columns(2)
            
            for idx, member in enumerate(COUNCIL_MEMBERS):
                with cols[idx % 2]:
                    st.markdown(f"### {member['name']} Approach")
                    response = get_council_response(question, member, rules)
                    
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
        st.warning("Please fill in at least: Recipient Name, Company Name, and Training Need")

# Footer
st.markdown("---")
st.markdown("💡 **Tips:**")
st.markdown("- Fill in as much context as possible for better personalization")
st.markdown("- Review all variations to find the tone that matches your relationship with the prospect")
st.markdown("- Always customize the generated email with specific details before sending")
