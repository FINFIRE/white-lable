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


def acceleratorpublic(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Accelerator</b></u><br>

    Capital Type: Public </center></p>

    <p><b><u>Introduction</u></b><br>

Public Accelerators are structured startup support programs backed by government bodies or public institutions that aim to stimulate entrepreneurship, innovation, and economic development. These programs provide early-stage startups with intensive mentorship, non-dilutive funding, and access to public-sector networks to help them commercialize products and prepare for future fundraising. Unlike purely private initiatives, public accelerators align startup growth with national or regional policy objectives such as job creation, sustainability, and digital transformation. {n} fits that definition. Public accelerators have played a significant role in global startup ecosystems for more than a decade. For instance, in 2023, the MaRS Discovery District in Canada supported over 1,200 ventures that collectively raised more than $2.4 billion CAD.¹ Since its launch in 2010, Startup Chile has invested over $80 million across more than 2,000 startups worldwide.² Similarly, the EIT Digital Accelerator in the European Union has helped startups raise over €900 million in funding, particularly in deep tech and innovation-driven sectors.³ On average, startups supported by public accelerators receive between $25,000 and $100,000 in grant or seed funding, in addition to business services valued at over $50,000. However, despite their benefits, the structured timelines, competitive selection processes, and alignment with public policy priorities may reduce flexibility for certain startups.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1. Public accelerators are publicly funded or government-supported programs that assist early-stage startups through cohort-based, time-limited initiatives. They offer structured mentorship, training, and non-dilutive financial support, along with access to public infrastructure, industry experts, and institutional networks. These programs often emphasize innovation-led growth, social impact, and regional development rather than short-term financial returns. Because funding originates from public sources, public accelerators usually do not take equity in participating startups, making them an attractive option for founders seeking growth capital without ownership dilution. (Faster Capital, n.d.)

<br>



    <br>2.  The most suitable companies for public accelerators are early-stage startups that focus on innovation, technology, or social impact and align with government development priorities such as sustainability, healthcare, digital infrastructure, and inclusive economic growth. These startups typically operate at the pre-seed to seed stage, possess a working prototype or minimum viable product (MVP), and are led by a capable and committed founding team. Public accelerators are particularly valuable for startups in underserved sectors or regions where private investment is limited, as they provide both funding and ecosystem support. Startups with clear impact goals and scalable business models tend to benefit the most. (WPAB, 2025)

<br>


    <br>3. Public accelerators gained prominence in the late 2000s as governments sought new ways to promote entrepreneurship and innovation following the global financial crisis. Inspired by the success of private accelerators such as Y Combinator and Techstars, public-sector versions were created to reduce entry barriers for early-stage startups, especially in regions lacking venture capital access. Startup Chile, launched in 2010, became one of the earliest and most influential public accelerator models, attracting global founders and diversifying the national economy. This success encouraged similar initiatives in Canada, Europe, Asia, and Africa. Over time, public accelerators have become central components of national innovation strategies, with increasing emphasis on climate tech, AI, health, and digital transformation. (ArtesianVC, 2021)

<br>

    <br>4. Despite their advantages, public accelerators present several challenges. Entry into these programs is highly competitive, with strict eligibility requirements that may not suit every startup’s stage or strategy. Founders may need to comply with fixed timelines, reporting requirements, or public-sector priorities, which can limit operational flexibility. In some cases, mentorship and support may be more standardized or bureaucratic compared to private accelerators. Furthermore, public funding is subject to political and budgetary changes, which can affect program continuity and long-term support. (The CEO Strategy, 2024)

<br>

    <br>5. 
To raise capital through a public accelerator, startups must complete a formal application process demonstrating innovation, scalability, and alignment with the program’s public mission. Most programs require evidence of early traction, a working MVP, and a committed founding team. Selected startups participate in structured programming, including mentorship, workshops, pilot projects, and progress reviews. Funding is typically provided in the form of grants or seed capital, accompanied by strict reporting and compliance requirements. Programs often conclude with demo days or evaluations that connect startups with investors, government agencies, and strategic partners. A strong application highlighting impact, market potential, and execution capability is critical for selection success. (PitchBob.io, n.d.)    </p>

                            

    <p><u><b>References</u></b><br>

    <br>FasterCapital. (n.d.). Government funding: How to access public funds and programs for your startup. <a href="https://fastercapital.com/content/Government-funding--How-to-access-and-benefit-from-public-funds-for-your-startup.html ">https://fastercapital.com/content/Government-funding--How-to-access-and-benefit-from-public-funds-for-your-startup.html </a>

<br>

    <br>WPAB. (2025). Social impact accelerators and public funding programs. <a href="https://www.failory.com/startups/social-impact-accelerators-incubators">https://www.failory.com/startups/social-impact-accelerators-incubators </a>

<br>

    <br>ArtesianVC. (2021). Timeline history: The evolution of startup incubators & accelerators. <a href="https://www.artesianinvest.com/post/timeline-history-the-evolution-of-startup-incubators-accelerators"> https://www.artesianinvest.com/post/timeline-history-the-evolution-of-startup-incubators-accelerators</a>

<br>

    <br>
The CEO Strategy. (2024). Are startup accelerators worth it? Pros & cons. <a href="https://slidebean.medium.com/are-startup-accelerators-worth-it f6e475f4fe0a?source=follow_footer---------3---------------------------- ">https://slidebean.medium.com/are-startup-accelerators-worth-it f6e475f4fe0a?source=follow_footer---------3---------------------------- </a>

<br>

    <br>
PitchBob.io. (n.d.). How to get accepted into ERA Accelerator. <a href="https://pitchbob.io/library/accelerators/how-to-get-accepted-into-era-accelerator-an-insider-s-guide-for-startup-founders-pitchbob-io ">https://pitchbob.io/library/accelerators/how-to-get-accepted-into-era-accelerator-an-insider-s-guide-for-startup-founders-pitchbob-io </a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Registered Business – Must be legally incorporated and in good standing
<br>•	Eligible Location – Must operate within the program’s jurisdiction
<br>•	Licenses & Tax Compliance – Valid business licenses and tax filings
<br>•	No Legal Disputes – No unresolved lawsuits or violations
<br>•	Founder Eligibility – Legal age and work authorization
<br>•	IP Ownership – Clear ownership of core intellectual property
<br>•	Clean Cap Table – No equity disputes or unclear ownership
<br>•	AML/KYC Compliance – Background and identity verification
<br>•	No Restricted Affiliations – Not linked to sanctioned entities
<br>•	Legal Documentation – NDAs, founder agreements, and policies
<br>•	Fund Use Oversight – Compliance with reporting and spending rules



    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Certificate of Incorporation – Legal registration proof
<br>•	Business License – Authorization to operate
<br>•	Cap Table – Ownership and equity structure
<br>•	Pitch Deck – Business, product, team, and traction
<br>•	Financial Statements – Historical or projected financials
<br>•	Founders’ Resumes/Bios – Experience and qualifications
<br>•	IP Ownership Proof – Patents, trademarks, or assignments
<br>•	Founders’ Agreement – Roles and equity splits
<br>•	Articles of Incorporation / Bylaws – Governing documents
<br>•	Market Validation Evidence – Surveys, pilots, or user metrics
<br>•	Terms of Service & Privacy Policy – For digital platforms



    </p>                                                                       
        """)
    introduction = mark_safe(introduction.format(n=name))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratorpublicfaq(request):
    introduction = mark_safe("""
     <p><b><center>Capital Market: Accelerator<br>

    Public</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is a public accelerator?</u></b><br>

    •Answer: A public accelerator is a startup acceleration program supported or funded by government bodies, public institutions, or non-profit organizations. Its primary objective is to promote innovation, economic development, and job creation by helping early-stage startups grow through structured mentorship, technical assistance, and access to public and private networks.
</p>

                            

     <p><u><b>2. How does a public accelerator differ from private accelerators or VC programs?</u></b><br>

    •Answer: Unlike private accelerators or venture capital firms, public accelerators are not primarily driven by profit maximization. They focus on capacity building, commercialization, and ecosystem development. Funding, if provided, is often non-dilutive or minimally dilutive, and programs place greater emphasis on long-term sustainability rather than rapid exits.
</p>


                            

    <p><u><b>3. What stage of companies are best suited for a public accelerator?</u></b><br>

    •Answer: Public accelerators typically support pre-revenue to early-revenue startups that have a defined problem, a prototype or minimum viable product (MVP), and early market validation. They are especially suitable for startups preparing for commercialization or future private investment.
</p>


                            

   <p><u><b>4. Do public accelerators provide funding?</u></b><br>

    •Answer: Yes, some public accelerators provide funding, but it is usually modest and structured as grants, stipends, milestone-based support, or small equity investments. Many programs prioritize non-financial support and investment readiness over direct capital deployment.
</p>


                            

    <p><u><b>5. How much funding can startups expect from a public accelerator?</u></b><br>

    •Answer: Funding amounts vary widely by country and program. Typical support ranges from small grants or stipends to seed-level funding. Compared to private accelerators, the financial component is often secondary to mentorship, infrastructure, and policy support.
</p>


                            

   <p><u><b>6. How quickly can startups access support after selection?</u></b><br>

    •Answer: Once selected, startups usually gain immediate or near-immediate access to program resources such as mentorship, workspace, and training. Any financial support is commonly released early in the program or upon achieving defined milestones.
</p>


                            

 <p><u><b>7. Do public accelerators require equity?</u></b><br>

    •Answer: Many public accelerators do not require equity. When equity is taken, it is generally lower than private accelerators and structured to align with public-interest goals rather than financial returns. Grant-based models are common.
</p>
                            

     <p><u><b>8. Can startups raise capital while participating in a public accelerator?</u></b><br>

    •Answer: Yes. Public accelerators actively encourage startups to pursue additional funding during or after the program. Demo days, investor introductions, and connections to public financing schemes are common features, with minimal restrictions on external fundraising.
</p>

                            

   <p><u><b>9. What types of support do public accelerators provide?</u></b><br>

    •Answer: Public accelerators offer structured mentorship, business development support, regulatory guidance, access to public research institutions, pilot programs, subsidized office space, and connections to investors, corporates, and government agencies.
</p>

                            

    <p><u><b>10. What happens at the end of a public accelerator program?</u></b><br>

    •Answer: At program completion, startups often present at demo days or evaluation panels. Follow-on support may include continued mentorship, referrals to private accelerators, access to public grants, or assistance with seed or Series-A readiness.
</p>

                        

   <p><u><b>11. What are the main benefits of joining a public accelerator?</u></b><br>

    •Answer: Key benefits include low or no equity dilution, access to public infrastructure and policy networks, credibility enhancement, long-term support orientation, and strong ecosystem integration. Public accelerators are particularly valuable for first-time founders.
</p>

                        

  <p><u><b>12. Are there risks associated with public accelerators?</u></b><br>

    •Answer: Risks include slower decision-making processes, limited funding size, and less aggressive growth pressure compared to private accelerators. Some programs may prioritize policy alignment over market speed.
</p>

                        

   <p><u><b>13. How does a public accelerator compare to angel investors?</u></b><br>

    •Answer: Public accelerators focus on mentorship, readiness, and ecosystem support, while angel investors primarily provide capital and strategic advice. Public accelerators often prepare startups to become investable for angels and VCs.
</p>

                        

 <p><u><b>14. What types of startups are commonly accepted into public accelerators?</u></b><br>

    •Answer: Public accelerators frequently support technology-driven, impact-oriented, and innovation-based startups in sectors such as fintech, healthtech, cleantech, agritech, education, and social enterprise.
</p>

                        

  <p><u><b>15. How can startups improve their chances of acceptance?</u></b><br>

    •Answer: Startups should demonstrate a clear problem-solution fit, social or economic impact potential, early validation, and alignment with the accelerator’s public mission. Strong teams and scalable models significantly improve acceptance prospects.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratorpublictwelve(request):
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
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Accelerator</b></u><br>

    Capital Type: Public</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

Public accelerators are best suited for startups at the pre-seed to early seed stage, typically ranging from late ideation to early revenue. These programs focus on validating product–market fit, strengthening business models, and preparing startups for external investment rather than supporting very early idea-stage ventures.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>
While C-Corps are preferred due to their investor-friendly structure, public accelerators may also accept LLCs or private limited companies, particularly in regions where C-Corp formation is uncommon. Sole proprietorships and informal partnerships are generally discouraged, as public accelerators emphasize scalability, governance, and long-term growth potential.

    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

Public accelerators typically target startups that have raised limited or no institutional funding. Small amounts of bootstrapped capital, grants, or angel funding are acceptable. However, startups that have completed large seed rounds or Series A funding are usually considered beyond the intended scope of these programs.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Most public accelerators allow prior non-dilutive funding such as government grants, university funding, or competition prizes. Previous equity-based funding is evaluated carefully, as excessive dilution or complex cap tables may conflict with accelerator investment terms or program objectives.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

Although public accelerators typically provide modest initial funding (often $20,000–$150,000), their primary value lies in investor access, demo days, and follow-on funding opportunities. Startups are expected to use the program as a platform to raise larger seed or early growth rounds post-graduation.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Public accelerators are most compatible with startups in the pre-seed or early seed round. These programs help founders refine traction metrics, pricing strategies, and growth plans rather than closing major investment rounds during the accelerator itself.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funding is generally provided in a single upfront tranche, sometimes followed by performance-based incentives or awards. This structure allows startups to focus on execution during the program while preparing for future capital raises.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds from public accelerators are intended strictly for business development activities, including:
<br>•	Product and technology development
<br>•	Market testing and customer acquisition
<br>•	Hiring key early team members
<br>•	Core operational expenses
Use of funds for personal expenses, unrelated investments, or debt repayment is typically prohibited and monitored.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Participation in a public accelerator involves moderate to high risk, including uncertainty around market adoption, dilution risk, and the pressure to achieve rapid milestones. Startups also face opportunity costs due to the intensive time commitment required by accelerator programs.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The effective cost of capital is moderate, as startups often exchange equity (typically 5–10%) for funding, mentorship, and network access. While financial costs are relatively low, founders must accept dilution and increased expectations for growth and performance.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Public accelerators usually charge little to no participation fees. However, startups should budget for indirect costs such as legal structuring, travel, accommodation (if in-person), and operational expenses, which may range from $2,000 to $9,000 depending on program requirements.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

The application and selection process generally takes 2–3 months. Once accepted, initial funding is typically disbursed within a few weeks. Follow-on capital depends on milestone achievement, demo day performance, and investor interest after program completion.
</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)