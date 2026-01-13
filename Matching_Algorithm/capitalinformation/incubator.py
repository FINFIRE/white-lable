from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases


def incubator(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Incubator</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Incubators are ideal for early-stage companies seeking strategic support, resources, and initial capital to validate and grow their business models. Designed to help startups refine their operations, incubators often provide access to office space, mentorship, legal and accounting resources, and connections to early investors. {n} aligns well with these objectives. Incubators have proven to be a valuable tool for emerging businesses over the past decade. For example, as of 2024, there are over 1,400 active incubators in the United States supporting early-stage ventures. In 2023, startups participating in incubator programs raised more than $1.1 billion in follow-on funding. According to a 2023 benchmarking report, companies graduating from incubators reported an average valuation of $7.5 million within two years of program completion. However, incubators can be highly competitive, and not all participants will gain funding or traction; startups must still execute effectively to realize the full benefits.  There are three types of incubator that we can match you with: 1) Private, 2) Public and 3) University. We will select the most appropriate incubator as per your business need.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Business incubators are organizations designed to support early-stage companies by providing a structured environment for growth and development. These programs typically offer a combination of resources, including office space, mentorship, business services, access to investors, and educational programming. Incubators aim to help startups validate their business models, refine their products or services, and become financially viable. Most incubators are time-bound (often 3 to 12 months) and focus on helping entrepreneurs reduce early-stage risk while accelerating their path to market. While highly beneficial, participation in an incubator often requires a competitive application process, and success is not guaranteed—startups must still demonstrate traction and execution to secure long-term funding and sustainability. (Business Incubator, 2025)
<br>
    <br>2. There are several types of incubators that businesses can use to raise capital, each tailored to different industries, stages of growth, or business models. University-based incubators often support student and faculty ventures, offering early-stage funding, research resources, and connections to academic investors. Corporate incubators, backed by large companies, help startups develop solutions aligned with the corporation’s strategic interests, often in exchange for equity or future partnerships. Non-profit and government-affiliated incubators focus on regional economic development and may provide grants or low-interest funding to startups in underserved areas. Private incubators are typically run by venture firms or accelerators and offer a more investment-driven model, providing capital in return for equity stakes. Additionally, industry-specific incubators—such as those focused on healthcare, fintech, or cleantech—connect startups with niche investors and partners who understand sector-specific challenges. These incubators not only help refine business models but also serve as a gateway to funding by preparing companies to pitch to angels, VCs, or strategic partners. (Team, 2023)
<br>
    <br>3. The concept of business incubators dates back to the late 1950s, with the first recognized incubator established in Batavia, New York, in 1959 by Joseph Mancuso at the Batavia Industrial Center. Originally created to repurpose a vacant industrial building and support local economic development, the model quickly gained traction as a way to nurture small businesses. Through the 1980s and 1990s, incubators began to spread across the U.S., often supported by universities, government agencies, and economic development organizations. By the early 2000s, the rise of tech startups and the dot-com boom gave incubators new prominence, especially in innovation hubs like Silicon Valley. Modern incubators have since evolved to specialize in industries such as biotech, fintech, and clean energy, offering not just space and mentorship, but structured programs, seed funding, and investor access. Today, incubators play a critical role in startup ecosystems worldwide, helping thousands of ventures launch and scale successfully. (Peters, 2017)
<br>
    <br>4. While business incubators offer valuable resources and support, there are several risks that companies should consider before joining. One key risk is misalignment—the goals or focus of the incubator may not fully match the startup’s vision, leading to strategic conflicts or misdirected growth. Equity dilution is another concern, as some incubators require ownership stakes in exchange for support, which can reduce the founder’s control and future fundraising flexibility. Additionally, overreliance on the incubator’s resources or mentorship can hinder a company’s ability to operate independently once the program ends. There’s also the risk of reputation by association, where being part of a lower-quality or poorly managed incubator could affect investor perception. Lastly, time and energy spent meeting incubator requirements or participating in programming may distract from core business operations, particularly if the incubator’s services don’t align with the startup’s immediate needs. (FasterCapital n.d.)
<br>
    <br>5. To qualify for a business incubator, a company typically needs to meet several key criteria. First, the business should be in the early stages of development, ideally a startup with a clear vision and potential for growth. Incubators usually look for companies that have a strong business idea or a minimum viable product (MVP), as they are focused on accelerating the development of viable products or services. A committed founding team with complementary skills and experience is also essential, as incubators often provide mentorship and resources to help founders refine their operations. Additionally, companies should be open to receiving mentorship, resources, and guidance from the incubator, as this is a significant part of the value they offer. Incubators may also require the company to be based in a specific location or industry, as some incubators focus on sectors like technology, healthcare, or cleantech. Finally, companies must be prepared to give up a small equity stake in exchange for the incubator’s support, although the percentage varies depending on the incubator’s structure. (Arc, 2023)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Business incubator. (2025, January 10). Entrepreneur. <a href="https://www.entrepreneur.com/encyclopedia/business-incubator?">https://www.entrepreneur.com/encyclopedia/business-incubator?</a>
<br>
    <br>Team, A., & Team, A. (2023, March 5). Understanding the different types of startup incubators and accelerators. AIContentfy. <a href="https://aicontentfy.com/en/blog/understanding-different-types-of-startup-incubators-and-accelerators?">https://aicontentfy.com/en/blog/understanding-different-types-of-startup-incubators-and-accelerators?</a>
<br>
    <br>Peters, J. (2017, June 28). The startup incubator was born on this 1950s egg farm. WIRED. <a href="https://www.wired.com/story/how-a-1950s-egg-farm-hatched-the-modern-startup-incubator/?">https://www.wired.com/story/how-a-1950s-egg-farm-hatched-the-modern-startup-incubator/?</a>
<br>
    <br>The Advantages and Disadvantages of start up incubation - FasterCapital. (n.d.). FasterCapital. <a href="https://fastercapital.com/content/The-Advantages-and-Disadvantages-of-Start-Up-Incubation.html">https://fastercapital.com/content/The-Advantages-and-Disadvantages-of-Start-Up-Incubation.html</a>
<br>
    <br>Arc. (2023, October 2). The Founder’s Guide to Startup Incubators in 2024 | ARC. Arc. <a href="https://www.joinarc.com/guides/startup-incubator?">https://www.joinarc.com/guides/startup-incubator?</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Stage of Development: Early-stage business with a clear idea or MVP.
    <br>• Committed Team: A dedicated, skilled founding team.
    <br>• Scalable Business: A product or service with growth potential.
    <br>• Willingness to Accept Mentorship: Openness to feedback and guidance from incubator mentors.
    <br>• Industry Focus: Alignment with the incubator’s sector (e.g., tech, healthcare).
    <br>• Equity Stake: Willingness to provide a small equity stake for incubator support.
    <br>• Location or Program Fit: Must meet geographical or program-specific requirements.
    <br>• Funding/Capital: May need to have raised initial capital or show investment interest.
    <br>• Growth Potential: A business that can grow significantly or disrupt its market.
    <br>• Application Process: Completion of the incubator’s application with necessary documentation (business plans, financials, etc.).
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan: A detailed description of the business model, market opportunity, and long-term vision.
    <br>• Financial Statements: Current financial data, including balance sheets, income statements, and cash flow projections.
    <br>• Pitch Deck: A concise, visually engaging presentation highlighting the business concept, team, and growth potential.
    <br>• Market Research: Evidence of market demand, customer analysis, and competitive landscape.
    <br>• Founder Resumes: Professional backgrounds of the founding team, highlighting relevant experience and skills.
    <br>• Product or MVP: Proof of concept, prototype, or minimum viable product to demonstrate feasibility.
    <br>• Equity and Ownership Structure: Documents outlining ownership percentages, share distribution, and any investor agreements.
    <br>• Legal Documents: Business registration, intellectual property filings, and any relevant legal agreements.
    <br>• Funding History: Details of any previous investments, grants, or other capital raised.
    <br>• References or Testimonials: Letters or endorsements from mentors, investors, or industry professionals.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatorfaq(request):
    introduction = mark_safe("""                    
    <p><b><u>FAQs</u></b></p>
                             
    <p><b><u>1. What is a business incubator?</u></b><br>
    • Answer: A business incubator is a program or organization that provides startups and early-stage companies with resources such as office space, mentorship, business services, networking, and sometimes funding, to help them grow and become self-sustaining.
    </p>
                             
    <p><b><u>2. Who should apply to a business incubator?</u></b><br>
    • Answer: Early-stage startups and companies with a minimum viable product (MVP), some traction, and a clear growth plan. Ideal candidates are looking for strategic support and access to industry networks rather than just capital.
    </p>
                             
    <p><b><u>3. What industries do incubators support?</u></b><br>
    • Answer: Incubators vary—some are generalists, while others specialize in industries like tech, healthcare, biotech, clean energy, food and beverage, or social impact ventures.
    </p>
                             
    <p><b><u>4. What are the benefits of joining an incubator?</u></b><br>
    • Answer: Incubators provide mentorship, structured programs, access to investors and industry experts, potential funding, shared workspaces, business services (legal, accounting, etc.), and increased credibility.
    </p>
                             
    <p><b><u>5. Do incubators take equity in the company?</u></b><br>
    • Answer: Some incubators operate on an equity-based model, taking a small percentage (typically 5–10%) of equity in exchange for participation. Others may charge a fee or operate through grants or public funding and take no equity.
    </p>
                             
    <p><b><u>6. How long does an incubator program last?</u></b><br>
    • Answer: Programs vary in length but usually last from 3 to 24 months. The duration depends on the program’s structure and the company’s development needs.
    </p>
                             
    <p><b><u>7. How competitive is the application process?</u></b><br>
    • Answer: Highly competitive. Acceptance rates can be as low as 5–10% for top-tier incubators. A strong business plan, team, traction, and market potential improve your chances.
    </p>
                             
    <p><b><u>8. Can I join an incubator if I’ve already raised funding?</u></b><br>
    • Answer: Yes, but most incubators prefer companies that haven’t raised large amounts of institutional capital. Companies with seed or angel funding are often still eligible.
    </p>
                             
    <p><b><u>9. What is the difference between an incubator and an accelerator?</u></b><br>
    • Answer: Incubators focus on early-stage development and provide long-term support. Accelerators are more intensive, short-term programs (typically 3–6 months) designed to rapidly scale startups, often culminating in a demo day.</p>
                             
    <p><b><u>10. Are virtual incubators available?</u></b><br>
    • Answer: Yes. Many incubators now offer remote or hybrid programs that provide mentorship, resources, and support online, making them accessible to startups outside of major cities.</p>                                        
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatortwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    premarketStr = ''

    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' :'additional fund might be required and incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'Minimum $500 - Maximum $999' :  'additional fund might be required and incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'Minimum $1000 - Maximum $2499' :  'incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'Minimum $2500 - Maximum $4999' :  'incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'Minimum $5000 - Maximum $9999' :  'incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'Minimum $10000 - Maximum $24999' : 'incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'Minimum $25000 - Maximum $49999' : 'incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',
        'More than $50000+' : 'incubator participation can deliver high ROI by compressing timelines and unlocking follow-on capital faster than solo development.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : '1 day to 1 week timeline is not in line with the time required for incubator program.',
        '1 Week to 2 Week' : '1 week to 2 week timeline might not be sufficent to raise capital through most incubator programs.',
        '2 Weeks to 4 Weeks' : '2 weeks to 4 weeks timeline might not be sufficent to raise capital through most incubator programs.',
        '1 Month to 2 Months' : '1 month to 2 months timeline might not be sufficent to raise capital through most incubator programs.',
        '2 Months to 3 Months' : '2 month to 3 months timeline is in line with the time required for incubator program.',
        '3 Months to 6 Months' : '3 month to 6 months timeline is in line with the time required for incubator program.',
        '6 Months to 12 Months' : '6 month to 12 months timeline is in line with the time required for incubator program.',
        'More than 1 year' : '6 month to 12 months timeline is in line with the time required for incubator program.',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    entity_options ={
         "None (To be Determined)" : "does not qualify for incubator capital market.",
         "Sole Proprietorship" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity).",
         "LLC" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity)." ,
         "LP" : "does not qualify for incubator capital market.",
         "GP" : "does not qualify for incubator capital market.",
         "S Corporation" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity).",
         "C Corp" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity).",
         "Other" : "does not qualify for incubator capital market.",
    }
    entityanalysis = entity_options[entity]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()   
   
    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Incubator</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As {n} enters an {stage} stage, participation in an incubator offers critical infrastructure, mentorship, and foundational resources to accelerate development. Ideal candidates include pre-revenue or pre-product startups with validated market potential, initial team formation, and a roadmap to MVP or customer discovery milestones.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Incubator programs typically support U.S.-based for-profit entities, including LLCs, C Corporations, or Sole Proprietorships—though C Corporations are often preferred due to their compatibility with venture investment and institutional support. {n} being {entity}, {n}’s legal structure {entityanalysis}
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} already secured in pre-capital, {n} demonstrates early traction and investor validation—qualities that increase competitiveness when applying to selective incubator cohorts. Access to non-dilutive resources through an incubator can extend the utility of this capital while reducing reliance on future early-stage equity rounds.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If {n}’s early capital came from {premarketstr}, incubator support can provide the structure and expertise needed to transition to an institutional seed round. This foundational backing makes {n} more attractive to future VCs and seed-stage investors, particularly when incubator affiliation includes demo days and investor introductions.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} intends to raise {raisegoal} over the next 12–18 months, incubators can act as a springboard—providing pitch readiness, financial modeling assistance, and milestone accountability. While incubators themselves may not invest large checks, their network effects can help unlock funding between $100K and $2M, depending on traction and sector.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Incubators typically support startups preparing for a Pre-Seed or Seed Round and are not intended for later-stage fundraising. For {n}, an incubator can position the business for its first institutional round by helping refine go-to-market strategy, customer acquisition channels, product-market fit, and data-backed KPIs.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Incubator-related capital is often deployed in a single upfront investment (if applicable) or through milestone-driven access to resources (office space, advisors, or grants). If {n} participates in an incubator that includes funding, the tranche schedule will be defined by internal metrics or program timelines (e.g., post-program raise, demo day targets).
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Incubator participation supports a wide range of strategic activities, including:
    <br>• Product development or MVP launch
    <br>• Market research and customer validation
    <br>• Legal structuring and compliance
    <br>• Talent acquisition and advisory support
    <br>• Fundraising preparation and investor readiness
    {n} should prepare a lean and focused use-of-funds plan aligning with these incubator-supported activities.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Participation in an incubator generally carries low financial risk, though reputational and opportunity risks exist. Poor performance in a highly visible program can affect future investor perception. For {n}, risk mitigation involves full engagement in program offerings, transparency with mentors, and rapid iteration based on feedback.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Most incubators operate under one of the following models:
    <br>• Equity-based (4%–7%) for program participation
    <br>• Non-dilutive (sponsored or government-backed)
    <br>• Tuition-based (fixed fee, often refundable upon completion or raise)

    For {n}, understanding the trade-offs between equity given and long-term value received is essential. Affiliation with a high-quality incubator can significantly improve valuation and investor access downstream.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Upfront costs are typically low but may include:
    <br>• Application or program fees ($0–$10,000 depending on the program)
    <br>• Legal restructuring if required for entry (e.g., Delaware C-Corp formation)
    <br>• Relocation or travel costs if the program is in-person
    <br>• An average total cost might fall between $0 to $2,500.

    If {n} has a {upfrontcost} allocated for early-stage development, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The typical application-to-enrollment timeline for incubators is 2–12 weeks, depending on the program. Once admitted, most programs run for 10–16 weeks, with Demo Day or investor introductions occurring at the conclusion. {n} can maximize success by preparing:
    <br>• A concise and compelling pitch deck
    <br>• Clearly defined goals and KPIs
    <br>• Evidence of customer discovery or MVP traction
    <br>• A flexible schedule for program participation
    Early preparation, clear value alignment, and strong storytelling will enhance acceptance rates and post-program funding success. {n}'s {timeanalysis}
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,timeanalysis=timeanalysis,premarketstr=premarketStr,entityanalysis=entityanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)