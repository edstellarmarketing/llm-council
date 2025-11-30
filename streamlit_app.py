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
EDSTELLAR_RULES = """# Edstellar Complete Email Response Rules Guide

## CRITICAL: Email Generation Requirements

### MANDATORY OUTPUT FORMAT
Every email MUST include ALL of the following components in this exact order:

1. **Subject Line** (on first line, prefixed with "Subject:")
2. **Email Body** containing:
   - Professional greeting with recipient's name
   - Context acknowledgment (reference their inquiry/training need)
   - Value proposition (2-3 sentences max)
   - Clear call-to-action
   - Professional closing with signature

### STRICT WORD COUNT LIMITS
- **Total Email Body**: 150-200 words maximum (NOT including subject line and signature)
- **Subject Line**: 50-60 characters maximum
- **Opening Paragraph**: 2-3 sentences
- **Value Proposition**: 2-3 sentences
- **Call-to-Action**: 1-2 sentences
- **Exceeding 200 words is a FAILURE** - be concise and impactful

## Core Response Principles

### Professional Tone Standards
- Warm but authoritative - balance approachability with expertise
- Consultative, not salesy - position as advisor, not vendor
- Confident without arrogance - demonstrate capability through specifics
- Respectful of recipient's time - get to the point quickly
- Partnership-focused - emphasize collaboration over transaction

### Response Timing Context
- **Initial Response**: Within 4-6 business hours of inquiry
- **Follow-up 1**: 3-4 business days if no response
- **Follow-up 2**: 7 days after first follow-up
- **Maximum touches**: 3 total (initial + 2 follow-ups)
- Always reference time context appropriately in email

## Subject Line Construction

### Format Rules
- Maximum 50-60 characters (mobile-optimized)
- Include recipient's company name when possible
- Action-oriented and specific
- No spam triggers (FREE, !!!, URGENT, Limited Time)
- Avoid generic phrases ("Quick Question", "Following Up")

### Proven Formulas
**For Course Inquiries:**
- "[Training Topic] Solutions for [Company]"
- "Customized [Topic] Training - [Company]"
- "RE: [Company]'s [Specific Training] Inquiry"

**For General Inquiries:**
- "Addressing [Company]'s Training Needs"
- "[Specific Outcome] Training for [Company]"
- "Partnership Opportunity: [Value Proposition]"

**For Follow-ups:**
- "RE: [Training Topic] Discussion - [Company]"
- "Following Up: [Specific Training] for [Team/Department]"
- "[Company] Training Solutions - Next Steps"

### Examples - Good vs Bad

**GOOD:**
- "Oracle EBS Training for REC Limited" (38 chars)
- "Customized Leadership Program - Acme Corp" (43 chars)
- "RE: Python Training Inquiry - TechStart" (39 chars)

**BAD:**
- "Following Up on Our Previous Email About Training" (too long, generic)
- "URGENT: Amazing Training Opportunity!!!" (spam triggers)
- "Quick Question" (too vague)

## Email Body Structure

### Opening (2-3 sentences, ~40-50 words)

**Components:**
1. Personalized greeting with correct name and title
2. Immediate context reference (their inquiry, specific need, or conversation)
3. Clear purpose statement

**Template:**
```
Dear [Title] [Last Name],

Thank you for your inquiry regarding [specific training topic] for [Company]. I understand you're looking for [specific requirement from their inquiry]. I'd like to share how Edstellar can support [Company]'s specific needs in this area.
```

**Examples:**

*For Course Page Inquiry:*
```
Dear Mr. Dangi,

Thank you for your interest in our Oracle EBS R12 Technical and DBA training for REC Limited. I understand you require on-site delivery for your team. I'd like to discuss how we can customize this program to address REC Limited's specific technical environment and learning objectives.
```

*For General Inquiry:*
```
Dear Ms. Patel,

Thank you for reaching out about leadership development training for your management team at Infosys. Based on your inquiry, I understand you're looking to strengthen strategic decision-making capabilities. I'd like to explore how Edstellar can design a program tailored to your organization's leadership framework.
```

### Value Proposition (2-3 sentences, ~60-80 words)

**Focus Areas:**
- Lead with CLIENT benefit, not Edstellar features
- Connect to their specific pain point or goal
- Use concrete outcomes, avoid vague claims
- Include 1 credibility marker if relevant

**Template:**
```
[Specific outcome relevant to their need]. With [relevant credential/experience], we've helped organizations like [similar example] achieve [specific result]. Our approach focuses on [key differentiator relevant to their need].
```

**Examples:**

*Technical Training:*
```
Our Oracle EBS R12 program combines hands-on labs with real-world scenarios specific to your production environment, ensuring your team can immediately apply their learning. We've successfully trained over 200 Oracle professionals across manufacturing and energy sectors, with an average 40% reduction in post-implementation support tickets. The program includes dedicated practice environments and post-training support.
```

*Leadership Development:*
```
Our customized leadership programs are designed around your specific business challenges and organizational culture, not generic leadership theory. We've partnered with 15+ Fortune 500 companies to develop their leadership pipelines, with 85% of participants promoted within 18 months. The program includes real-time application to your actual strategic initiatives.
```

### Call-to-Action (1-2 sentences, ~30-40 words)

**Guidelines:**
- Single, clear next step
- Low commitment ask (15-30 minute call)
- Provide specific options when possible
- Make it easy to say yes

**Templates:**

*Initial Response:*
```
Would you be available for a brief 20-minute call this week to discuss your specific requirements? I have availability Thursday afternoon or Friday morning and can work around your schedule.
```

*Alternative (more direct):*
```
I'd love to share some specific examples of how we've addressed similar needs. Are you available for a quick call on [Day] at [Time] or [Alternative Day/Time]?
```

*For Technical Decision Makers:*
```
I can walk you through our technical approach and customization options in a brief 20-minute discussion. Would next Tuesday or Wednesday work for a quick call?
```

### Closing & Signature

**Format:**
```
[Sign-off],

[Your Full Name]
[Your Title]
Edstellar
[Phone Number]
[Email Address]
```

**Sign-off Options by Context:**
- **Standard**: "Best regards," or "Warm regards,"
- **More Formal (C-Suite)**: "Respectfully," or "Sincerely,"
- **Warmer (Ongoing Relationship)**: "Looking forward to connecting,"

**Example:**
```
Best regards,

Vijay Kumar
Marketing Manager
Edstellar
+91 [Phone Number]
vijay@edstellar.com
```

## Language & Tone Guidelines

### Words & Phrases to USE

**Action-Oriented:**
- "Discuss," "Explore," "Share," "Design," "Customize"
- "Address," "Support," "Develop," "Strengthen"
- "Achieve," "Implement," "Apply," "Deliver"

**Value-Focused:**
- "Tailored to your needs"
- "Specific to your environment"
- "Designed around your goals"
- "Aligned with your objectives"
- "Relevant to your context"

**Outcome-Oriented:**
- "Immediate application"
- "Measurable results"
- "Practical skills"
- "Real-world application"
- "Sustainable impact"

### Words & Phrases to AVOID

**Overused/Generic:**
- ❌ "World-class" / "Best-in-class"
- ❌ "Cutting-edge" / "State-of-the-art"
- ❌ "Revolutionize" / "Transform" / "Disrupt"
- ❌ "Turnkey solution"
- ❌ "One-stop shop"

**Weak/Apologetic:**
- ❌ "Just checking in"
- ❌ "Just wanted to follow up"
- ❌ "Sorry to bother you"
- ❌ "I hope this email finds you well" (overused)
- ❌ "Per my last email"

**Pushy/Aggressive:**
- ❌ "Limited time offer"
- ❌ "Act now"
- ❌ "Don't miss out"
- ❌ "Opportunity of a lifetime"
- ❌ Multiple exclamation points!!!

## Tone Calibration by Recipient Level

### C-Suite / Senior Leadership

**Characteristics:**
- Ultra-concise (120-150 words maximum)
- Strategic focus (ROI, competitive advantage, business outcomes)
- No feature lists or technical details
- Reference board-level priorities
- Acknowledge extreme time constraints

**Example Opening:**
```
Dear Ms. Chen,

Thank you for your inquiry about executive leadership development for your senior team. I understand you're focused on strengthening strategic agility across your leadership bench as you scale into new markets.
```

**Value Proposition Focus:**
- Business impact and ROI
- Competitive positioning
- Strategic capability building
- Risk mitigation
- Speed to results

### HR / L&D Professionals

**Characteristics:**
- Moderate length (150-180 words)
- Focus on implementation, learner experience, and metrics
- Emphasize ease of coordination and support
- Mention reporting and measurement
- Reference best practices and standards

**Example Opening:**
```
Dear Mr. Sharma,

Thank you for reaching out about technical training for your IT team. I understand you're looking for a solution that minimizes disruption while maximizing skill development and can demonstrate clear learning outcomes.
```

**Value Proposition Focus:**
- Learner engagement and outcomes
- Implementation ease
- Customization process
- Measurement and reporting
- Post-training support

### Technical Managers / Subject Matter Experts

**Characteristics:**
- Can include more detail (180-200 words)
- Highlight technical depth and instructor expertise
- Mention specific methodologies and tools
- Focus on hands-on application
- Reference technical credentials

**Example Opening:**
```
Dear Dr. Kumar,

Thank you for your interest in our Oracle EBS R12 Technical training. I understand you need comprehensive coverage of both technical architecture and DBA functions, with hands-on labs using your actual system configuration.
```

**Value Proposition Focus:**
- Technical depth and accuracy
- Instructor credentials and experience
- Hands-on components
- Real-world application
- Technical support availability

## Personalization Requirements

### Minimum (MANDATORY) Personalization

Every email MUST include:
1. ✅ Correct recipient name with appropriate title (Mr./Ms./Dr.)
2. ✅ Correct company name spelled exactly as they provided
3. ✅ Specific training topic or need from their inquiry
4. ✅ Reference to HOW they contacted you (course page, contact form, etc.)
5. ✅ At least ONE specific detail from their inquiry

**UNACCEPTABLE:**
- Generic greetings: "Dear Sir/Madam," "To Whom It May Concern," "Hello,"
- Wrong name spelling or title
- Wrong company name
- Generic "training needs" without specifics

### Advanced Personalization (When Information Available)

**Company Context:**
- Recent news (expansion, funding, leadership changes)
- Industry challenges or trends
- Company size, structure, or stage
- Geographic locations or markets

**Role-Specific:**
- Department or team structure
- Current initiatives or projects
- Specific challenges in their role
- Reporting structure if known

**Inquiry-Specific:**
- Source page or content they viewed
- Specific questions they asked
- Timeline or urgency indicators
- Budget or scope hints

**Example with Advanced Personalization:**
```
Dear Mr. Patel,

Thank you for your inquiry about Change Management training for Tata Steel's transformation initiative. I noticed your recent announcement about the digital transformation program across your manufacturing operations, and I understand this training would support your frontline managers in leading their teams through these changes.
```

## Response Scenarios & Adaptations

### Scenario 1: Course Page Inquiry

**Context:** Someone submitted an inquiry from a specific course page

**Approach:**
- Reference the specific course by name
- Acknowledge their interest in that particular topic
- Mention customization options relevant to the course
- Offer to discuss their specific application needs

**Template:**
```
Subject: [Course Topic] Training for [Company]

Dear [Name],

Thank you for your interest in our [Specific Course Name] training for [Company]. I understand you're looking to [specific need from inquiry, e.g., "develop your team's capabilities in this area" or "address specific challenges with current processes"].

This program can be fully customized to address [Company]'s specific [context/environment/challenges]. We typically adapt the curriculum to include [relevant customization examples], ensuring your team can immediately apply the learning to your actual [projects/systems/processes]. With [relevant credential], we've helped [number] organizations in [industry] achieve [specific outcome].

Would you be available for a brief 20-minute call this week to discuss your specific requirements and how we can tailor the program? I have availability Thursday afternoon or Friday morning.

Best regards,
[Your Name]
```

### Scenario 2: General Training Inquiry

**Context:** Open-ended inquiry about training needs without specific course

**Approach:**
- Acknowledge their training objective
- Ask smart qualifying questions if needed
- Propose needs assessment or consultation
- Avoid jumping to solutions too quickly

**Template:**
```
Subject: Addressing [Company]'s [Training Area] Needs

Dear [Name],

Thank you for reaching out about [general training area] for your team at [Company]. I understand you're looking to [general objective from inquiry].

To ensure we design the most effective solution, I'd like to understand more about [specific aspect of their need]. Our approach typically starts with a brief needs assessment to identify [specific factors], which allows us to create a program that addresses your unique [challenges/goals/context]. We've worked with [number] organizations in [industry] to develop customized solutions that deliver [specific outcome].

Would you be available for a 20-minute discovery call this week? I can share how we've approached similar needs and discuss the best path forward for [Company].

Best regards,
[Your Name]
```

### Scenario 3: Specific Event/Workshop Request

**Context:** Request for specific training event, workshop, or program

**Approach:**
- Confirm understanding of their requirements
- Outline high-level approach
- Mention relevant past successes (without over-promising)
- Provide clear next steps

**Template:**
```
Subject: [Event/Workshop Type] for [Company] - Next Steps

Dear [Name],

Thank you for your request regarding [specific event/workshop] for [Company] on [date/timeframe]. I understand you're looking for [specific format/duration/objectives] to [their stated goal].

Based on your requirements, we would design a [format] that focuses on [key areas from their request]. Our approach would include [brief outline of methodology] to ensure [specific outcome they mentioned]. We've successfully delivered similar programs for [relevant example], achieving [specific result].

I'd like to schedule a brief call to discuss the specific content areas, participant profiles, and logistics. This will allow us to prepare a detailed proposal that precisely addresses your needs. Are you available for a 30-minute discussion on [day] or [alternative day]?

Best regards,
[Your Name]
```

### Scenario 4: On-Site Training Request

**Context:** Specific request for training at their location

**Approach:**
- Acknowledge on-site requirement
- Mention logistics flexibility
- Highlight benefits of on-site customization
- Address common on-site concerns proactively

**Template:**
```
Subject: On-Site [Topic] Training for [Company]

Dear [Name],

Thank you for your inquiry about on-site [training topic] for [Company]. I understand you need the training delivered at your [location] facility to accommodate your team's schedule and operational requirements.

Our on-site programs offer the advantage of incorporating your actual [systems/processes/scenarios] into the training, making it immediately applicable. We handle all logistics and can work around your operational schedule. With [relevant experience], we've successfully delivered on-site training across [number] locations in [region/industry], consistently achieving [specific outcome].

I'd like to discuss the specific learning objectives, participant profiles, and scheduling preferences to ensure we design the most effective program. Would you have 20 minutes this week for a brief call?

Best regards,
[Your Name]
```

## Follow-Up Guidelines

### Follow-Up #1 (3-4 Business Days After Initial Email)

**Purpose:** Gentle reminder with added value

**Approach:**
- Brief reference to original email
- Add NEW value (insight, resource, case study)
- More direct CTA
- Keep shorter than original (100-120 words)

**Template:**
```
Subject: RE: [Original Subject]

Dear [Name],

I wanted to follow up on my email from [day] regarding [training topic] for [Company]. 

I thought you might find it helpful to see how we recently worked with [similar company/industry] on a similar need. They achieved [specific result] within [timeframe] by focusing on [specific approach]. I'd be happy to share more details on how this might apply to your situation.

Are you available for a brief call this week? I have openings Thursday at 2pm or Friday at 10am.

Best regards,
[Your Name]
```

### Follow-Up #2 (7 Days After First Follow-Up)

**Purpose:** Final professional attempt with easy exit

**Approach:**
- Acknowledge multiple touchpoints
- Offer alternative (different resource, timing, connection)
- Include respectful "opt-out" language
- Keep very brief (80-100 words)

**Template:**
```
Subject: Final Follow-Up: [Training Topic] for [Company]

Dear [Name],

I understand you're likely busy with other priorities. I wanted to reach out one final time regarding [training topic] for [Company].

If timing isn't right now, I'm happy to reconnect in [timeframe]. Alternatively, if there's someone else at [Company] who handles [training area], I'd appreciate an introduction.

If you'd prefer not to receive further emails on this topic, just let me know and I'll note that in our system.

Best regards,
[Your Name]
```

### When to Stop Following Up

**Hard Stop Signals:**
- Explicit "not interested" response
- Request to stop contact
- Three emails sent with no response
- Email bounces or auto-responses indicate they've left

**Wait Period Before Re-Engagement:**
- After 3 emails with no response: Wait 3-6 months
- After explicit "not now": Wait until their indicated timeframe
- After role change: Appropriate to reach out to new contact

## Quality Assurance Checklist

### Before Sending - EVERY Email Must Pass:

**Personalization Check:**
- [ ] Recipient name spelled correctly with appropriate title
- [ ] Company name spelled exactly as they provided it
- [ ] Specific training topic/need referenced (not generic)
- [ ] At least one detail from their inquiry mentioned
- [ ] Source/origin of inquiry acknowledged

**Structure Check:**
- [ ] Subject line present and under 60 characters
- [ ] Professional greeting with name
- [ ] Clear purpose stated in first 2 sentences
- [ ] Value proposition included (2-3 sentences)
- [ ] Single, clear call-to-action
- [ ] Professional closing with complete signature

**Content Check:**
- [ ] Total word count 150-200 words (not including subject/signature)
- [ ] No generic claims or buzzwords
- [ ] Specific outcomes or benefits mentioned
- [ ] At least one credibility marker (if relevant)
- [ ] Tone appropriate for recipient level

**Technical Check:**
- [ ] No spelling or grammatical errors
- [ ] All links functional (if included)
- [ ] Mobile-friendly formatting (short paragraphs)
- [ ] Proper spacing and readability
- [ ] Professional email signature included

**Compliance Check:**
- [ ] No spam trigger words in subject line
- [ ] Unsubscribe/opt-out mention in follow-ups
- [ ] Accurate claims and representations
- [ ] Respect for privacy and data

### Red Flags - Auto-Reject if Present:

**Critical Errors:**
- ❌ Wrong recipient name or company name
- ❌ Generic greeting ("Dear Sir/Madam")
- ❌ No specific reference to their inquiry
- ❌ Over 200 words in email body
- ❌ Multiple CTAs or confusing next steps
- ❌ Spelling or grammar errors

**Major Issues:**
- ❌ Generic value proposition (could apply to anyone)
- ❌ No clear purpose in opening
- ❌ Overly long paragraphs (>4 sentences)
- ❌ Excessive "I/we" vs "you/your" ratio
- ❌ Attachment without context (in cold emails)
- ❌ Requesting >30 minutes initially

## Context-Specific Talking Points

### Edstellar Differentiators - When to Use What

**14 Years Experience:**
- Use when: Credibility needed, new relationship, enterprise prospects
- Don't use when: Startup/young company (may seem too corporate)
- Example: "With 14 years of corporate training experience, we've refined our approach to address the specific challenges organizations face when..."

**5,000+ Expert Trainers:**
- Use when: Specialized expertise needed, multiple locations, scale concerns
- Don't use when: Single small workshop, hyper-specialized niche
- Example: "Our global network of 5,000+ expert trainers ensures we can match you with specialists in [specific area] who have direct industry experience..."

**100+ Locations:**
- Use when: Multi-location delivery, international presence, on-site needs
- Don't use when: Single virtual session, one location only
- Example: "With presence in 100+ locations globally, we can deliver consistent on-site training across your facilities in [regions]..."

**Fortune 500 Experience:**
- Use when: Enterprise prospects, quality/scale concerns, risk-averse buyers
- Don't use when: Small business (may seem too expensive/corporate)
- Example: "We've partnered with Fortune 500 companies including [relevant industry] to develop and deliver training programs that meet enterprise standards for quality and measurability..."

**Customization Expertise:**
- Use when: ALWAYS - this is core differentiator
- Example: "Every program is tailored to your specific business context - we incorporate your actual [processes/systems/scenarios] into the curriculum..."

### Industry-Specific Approaches

**Manufacturing:**
- Focus on: Operational efficiency, safety, hands-on skills, shift scheduling
- Mention: On-site delivery, minimal disruption, production environment training
- Avoid: Pure theory, long duration programs

**Technology/IT:**
- Focus on: Technical depth, latest methodologies, practical application
- Mention: Instructor credentials, hands-on labs, post-training support
- Avoid: Generic business training language

**Financial Services:**
- Focus on: Compliance, risk management, regulatory requirements
- Mention: Industry-specific scenarios, confidentiality, certification options
- Avoid: Oversimplification of complex topics

**Healthcare:**
- Focus on: Patient outcomes, compliance, evidence-based practices
- Mention: Clinical applicability, scheduling flexibility, continuing education credits
- Avoid: Business jargon, non-clinical examples

**Professional Services:**
- Focus on: Client impact, billable efficiency, competitive differentiation
- Mention: ROI, application to client work, thought leadership
- Avoid: Generic corporate training positioning

## Response Handling Protocols

### Positive Response - They Want to Talk

**Timeline:** Respond within 4 business hours maximum

**Template:**
```
Dear [Name],

Excellent! I'm looking forward to our discussion about [topic] for [Company].

[If they suggested time:] [Day] at [Time] works perfectly for me. I'll send a calendar invitation with dial-in details.

[If you're suggesting times:] I have the following times available this week:
- [Day] at [Time]
- [Day] at [Time]  
- [Day] at [Time]

Please let me know which works best for you and I'll send the calendar invitation.

To make our time most productive, could you briefly share:
1. [Relevant question about their specific need]
2. [Relevant question about their context/timeline]

Looking forward to speaking with you.

Best regards,
[Your Name]
```

### Request for More Information

**Timeline:** Respond within 4-6 business hours

**Approach:**
- Provide requested information concisely
- Add ONE relevant resource/example
- Restate clear next step
- Make scheduling easy

**Template:**
```
Dear [Name],

Thank you for your response. Here's the information you requested about [topic]:

[Concise answer to their specific question - 2-3 sentences maximum]

I've also attached [relevant resource] that provides [specific value]. 

The best way to address your specific situation would be a brief conversation where I can understand your exact requirements and share relevant examples. Would you be available for 20 minutes this week? [Provide 2-3 specific time options]

Best regards,
[Your Name]
```

### Pricing Question

**Approach:**
- Acknowledge the question
- Explain that pricing depends on customization
- Offer to provide detailed quote after discussion
- Provide helpful range if possible

**Template:**
```
Dear [Name],

Thank you for asking about pricing. Because we customize each program to the specific needs, participant count, delivery format, and duration, our pricing varies accordingly.

For [type of program] similar to what you're describing, programs typically range from [low range] to [high range] depending on [key variables]. 

I'd be happy to provide you with a detailed quote that addresses your specific requirements. Would you have 20 minutes this week to discuss the details so I can prepare an accurate proposal?

Best regards,
[Your Name]
```

### "Not Interested" Response

**Approach:**
- Thank them professionally
- Ask if timing is the issue (leave door open)
- Request referral if appropriate
- Confirm no further contact if they prefer

**Template:**
```
Dear [Name],

Thank you for letting me know. I appreciate you taking the time to respond.

If it's a matter of timing, I'm happy to reach back out in [3/6] months when it might be more relevant. Otherwise, if there's someone else at [Company] who handles [training area], I'd appreciate an introduction.

Either way, thank you for considering Edstellar.

Best regards,
[Your Name]
```

### No Response After 3 Attempts

**Action:**
- Note in CRM: "3 attempts, no response - wait 6 months"
- Send final automated email if using sequences
- Do NOT continue emailing
- Wait 6 months before any re-engagement

## Email Template Library

### Template 1: Technical Training Course Inquiry Response
```
Subject: [Course Name] Training for [Company]

Dear [Title] [Last Name],

Thank you for your inquiry about our [Specific Course Name] training for [Company]. I understand you're looking to [specific need from inquiry - e.g., "build your team's expertise in this technology" or "prepare for upcoming implementation"].

This program can be customized to focus on [relevant aspects based on inquiry], incorporating your actual [systems/environment/scenarios] into hands-on labs. We've trained [number] professionals in [technology/topic] across [industry/region], with participants typically achieving [specific outcome] within [timeframe]. The program includes [key feature relevant to their need] and post-training support.

Would you be available for a brief 20-minute call this week to discuss your specific technical environment and learning objectives? I have availability Thursday afternoon or Friday morning and can work around your schedule.

Best regards,

[Your Name]
[Title]
Edstellar
[Phone]
[Email]
```

### Template 2: Leadership/Soft Skills Inquiry Response
```
Subject: [Leadership Topic] Program for [Company]

Dear [Title] [Last Name],

Thank you for reaching out about [leadership topic] training for [Company]. I understand you're focused on [specific goal from inquiry - e.g., "developing your emerging leaders" or "strengthening strategic thinking capabilities"].

Our approach to [topic] development is built around your specific organizational context and challenges, not generic leadership theory. We work with your actual strategic initiatives and business scenarios to ensure immediate application. We've partnered with [number] organizations in [industry] to develop leadership capabilities, with [percentage] of participants demonstrating measurable improvement in [specific area] within [timeframe].

I'd love to discuss how we can design a program that aligns with [Company]'s leadership framework and business priorities. Would you have 20 minutes this week for a brief call? I'm available [day] at [time] or [alternative].

Best regards,

[Your Name]
[Title]
Edstellar
[Phone]
[Email]
```

### Template 3: On-Site Training Request Response
```
Subject: On-Site [Topic] Training for [Company]

Dear [Title] [Last Name],

Thank you for your inquiry about on-site [training topic] training at [Company]'s [location] facility. I understand you need [specific requirement - e.g., "to accommodate your team's operational schedule" or "to use your actual equipment/systems in the training"].

On-site delivery allows us to incorporate your specific [environment/processes/scenarios] directly into the program, making it immediately applicable to your daily operations. We can work around your [shift schedule/production requirements/operational constraints] and handle all logistics. With [number] on-site programs delivered across [region/industry], we have extensive experience adapting to different facility requirements while maintaining training effectiveness.

I'd like to discuss the learning objectives, participant profiles, and scheduling preferences to design the most effective program for your team. Would you be available for a 20-minute call this week?

Best regards,

[Your Name]
[Title]
Edstellar
[Phone]
[Email]
```

### Template 4: General Corporate Training Inquiry
```
Subject: Addressing [Company]'s Training Needs

Dear [Title] [Last Name],

Thank you for your inquiry about training solutions for [Company]. I understand you're looking to [general objective from inquiry].

To ensure we design the most effective program, I'd like to better understand your specific goals around [aspect of their need]. Our approach typically starts with identifying your unique [business context/challenges/objectives], which allows us to create a solution that delivers measurable impact. We've worked with [number] organizations to develop customized training programs that achieve [relevant outcome].

Would you be available for a 20-minute discovery call this week? I can share how we've approached similar needs and discuss the best path forward for [Company]. I'm available [day/time options].

Best regards,

[Your Name]
[Title]
Edstellar
[Phone]
[Email]
```

## FINAL CHECKLIST - USE BEFORE EVERY EMAIL

### Content Accuracy
- [ ] All information from inquiry correctly captured
- [ ] Company and individual names spelled correctly
- [ ] Training topic/need accurately reflected
- [ ] No assumptions made beyond what's in inquiry

### Structure & Format
- [ ] Subject line under 60 characters
- [ ] Email body 150-200 words (excluding signature)
- [ ] Clear opening with context (2-3 sentences)
- [ ] Focused value proposition (2-3 sentences)
- [ ] Single, clear call-to-action (1-2 sentences)
- [ ] Professional closing and complete signature

### Personalization & Relevance
- [ ] Specific details from inquiry referenced
- [ ] Tone appropriate for recipient level
- [ ] Industry-relevant examples or language used
- [ ] At least one unique detail (not template language)

### Professional Standards
- [ ] No spelling or grammar errors
- [ ] No spam trigger words
- [ ] Professional but warm tone
- [ ] Appropriate formality level
- [ ] Mobile-friendly formatting

### Edstellar Brand Alignment
- [ ] Positions as partnership, not transaction
- [ ] Emphasizes customization appropriately
- [ ] Includes relevant credibility markers
- [ ] Maintains consultative approach
- [ ] Respects recipient's time and decision process"""

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
