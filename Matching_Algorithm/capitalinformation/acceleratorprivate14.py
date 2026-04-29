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


def acceleratorprivate(request):
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Accelerator</b></u><br>

    Capital Type: Private  </center></p>

    <p><b><u>Introduction</u></b><br>

Private accelerators are privately funded, for-profit programs designed to support early-stage startups through intensive, time-bound mentorship, seed investment, and access to investor and industry networks. Unlike public accelerators, private accelerators are typically operated by venture capital firms, corporations, or independent accelerator organizations and are driven primarily by financial return objectives. {n} fits that definition. Private accelerators have become a central component of global startup ecosystems since the early 2000s. Well-known examples such as Y Combinator, Techstars, and 500 Global have collectively supported thousands of startups and helped create companies valued at billions of dollars. According to Startup Genome, startups graduating from top private accelerators are significantly more likely to raise follow-on venture capital compared to non-accelerated startups. While private accelerators offer strong investor access and rapid scaling opportunities, they usually require equity participation and operate under highly competitive selection processes.
 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	Private accelerators are cohort-based startup programs funded and operated by private entities that provide early-stage companies with seed capital, structured mentorship, business development support, and investor exposure in exchange for equity. These programs typically run for a fixed duration—commonly between three and six months—and culminate in a demo day where startups pitch to angel investors and venture capital firms. Unlike public accelerators, private accelerators are profit-oriented and focus on identifying high-growth startups with scalable business models and strong exit potential (Y Combinator, n.d.).

<br>



    <br>2.	Private accelerators are best suited for high-growth, innovation-driven startups that aim to raise venture capital and scale rapidly. These companies are often technology-focused and operate in sectors such as software, fintech, health tech, artificial intelligence, e-commerce, and digital platforms. Typically, participating startups are at the pre-seed or seed stage, possess a minimum viable product (MVP), and are led by committed founding teams with strong execution capability. Private accelerators favor startups with large addressable markets and clear revenue or growth trajectories, as these characteristics align with investor return expectations (NVCA, 2022).

<br>


    <br>3.	Private accelerators emerged in the early 2000s, with Y Combinator’s launch in 2005 widely regarded as a turning point in early-stage startup financing. The accelerator model proved effective in reducing startup failure rates by combining capital, mentorship, and investor access into a compressed timeframe. Following the success of Y Combinator, numerous private accelerators were established globally, including Techstars and 500 Global, contributing to the rapid institutionalization of accelerator-based venture formation. Over time, private accelerators have become integral to venture capital pipelines and innovation ecosystems, particularly in technology-driven markets (ArtesianVC, 2021).

<br>

    <br>4.	Despite their advantages, private accelerators present several risks and limitations. The most significant drawback is equity dilution, as startups are required to give up ownership in exchange for relatively small amounts of seed capital. Participation also demands intense time commitment, which may distract founders from product development or customer acquisition. Additionally, accelerator quality varies widely, and not all programs provide meaningful mentorship or investor access. Over-reliance on accelerator branding without strong fundamentals may limit long-term success. Competitive selection processes also mean that many viable startups may not gain admission (The CEO Strategy, 2024).

<br>

    <br>5.	To raise capital through a private accelerator, startups must apply through a competitive selection process that evaluates the founding team, product, market opportunity, traction, and scalability. Selected startups receive seed investment—commonly ranging from USD 20,000 to USD 150,000—in exchange for equity stakes typically between 5% and 10%. During the program, startups participate in structured mentorship, workshops, and milestone reviews. The program concludes with a demo day, where startups pitch to investors for follow-on funding. Successful participation often leads to angel or venture capital investment shortly after graduation (Techstars, n.d.).
    </p>

                            

   <p><u><b>References</u></b><br>

    <br>Y Combinator. (n.d.). About Y Combinator. <a href=" https://www.ycombinator.com"> https://www.ycombinator.com</a>

<br>

     <br>National Venture Capital Association (NVCA). (2022). Seed-stage investment trends.  <a href="National Venture Capital Association (NVCA). (2022). Seed-stage investment trends. https://nvca.org">National Venture Capital Association (NVCA). (2022). Seed-stage investment trends. https://nvca.org</a>

<br>

   <br>ArtesianVC. (2021). Timeline history: The evolution of startup incubators & accelerators.  <a href="https://www.artesianinvest.com">https://www.artesianinvest.com</a>

<br>

   <br>The CEO Strategy. (2024). Are startup accelerators worth it? <a href=" https://theceostrategy.com"> https://theceostrategy.com</a>

<br>

   <br>Techstars. (n.d.). How the Techstars accelerator works. <a href=" https://www.techstars.com"> https://www.techstars.com</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Legally incorporated private company
<br>•	Clean and transparent capitalization table
<br>•	Founder consent to equity dilution
<br>•	Compliance with securities regulations
<br>•	Ability to execute accelerator equity agreements
<br>•	No unresolved legal or regulatory disputes




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Certificate of incorporation
<br>•	Pitch deck
<br>•	Capitalization table
<br>•	Founders’ resumes or bios
<br>•	Product demo or MVP documentation
<br>•	Financial projections
<br>•	Shareholder and equity agreements




    </p>                                                                     
        """)


    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratorprivatefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Accelerator<br>

    Private</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is a private accelerator?</u></b><br>

    •Answer: A private accelerator is a for-profit startup acceleration program operated by private organizations, venture capital firms, corporates, or independent accelerator operators. Its primary goal is to rapidly scale early-stage startups and generate financial returns through equity ownership.
</p>

                            

     <p><u><b>2. How does a private accelerator differ from a public accelerator?</u></b><br>

    •Answer: Private accelerators are profit-driven and typically take equity in exchange for capital and intensive support. Public accelerators focus on ecosystem development and may be non-dilutive. Private accelerators emphasize growth, traction, and investor readiness within a short timeframe.
</p>


                            

    <p><u><b>3. What stage of startups are best suited for private accelerators?</u></b><br>

    •Answer: Private accelerators are best suited for early-stage startups with a validated product, MVP, or early traction. Companies should be ready to scale, test markets quickly, and pursue follow-on investment.
</p>


                            

   <p><u><b>4. Do private accelerators provide funding?</u></b><br>

    •Answer: Yes. Most private accelerators provide seed capital at the start of the program. Funding is typically provided in exchange for equity and may be structured as direct equity, SAFE, or convertible notes.
</p>


                            

    <p><u><b>5. How much funding can startups expect from a private accelerator?</u></b><br>

    •Answer: Funding amounts vary by program but generally fall within a standard seed-stage range. The capital is intended to support rapid experimentation, hiring, and market entry during the accelerator period.
</p>


                            

   <p><u><b>6. How quickly can startups access funding?</u></b><br>

    •Answer: Funding is usually provided immediately upon acceptance or at the start of the program, allowing startups to focus on execution from day one.
</p>


                            

 <p><u><b>7. Do private accelerators require equity?</u></b><br>

    •Answer: Yes. Private accelerators typically take an equity stake, commonly in the single-digit percentage range. This equity compensates the accelerator for capital, mentorship, and network access.
</p>
                            

     <p><u><b>8. Can startups raise additional funding during a private accelerator?</u></b><br>

    •Answer: Yes. Private accelerators actively encourage startups to raise follow-on capital during or after the program. Demo days and investor pitch events are core components of most private accelerators.
</p>

                            

   <p><u><b>9. What types of support do private accelerators provide?</u></b><br>

    •Answer: Support includes intensive mentorship, growth strategy guidance, product and market validation, pitch coaching, investor introductions, legal and fundraising support, and access to a strong alumni and investor network.
</p>

                            

    <p><u><b>10. How long do private accelerator programs typically last?</u></b><br>

    •Answer: Private accelerator programs are time-bound, usually lasting between 8 to 16 weeks. The fixed duration creates urgency and focusses on measurable growth milestones.
</p>

                        

   <p><u><b>11. What happens after the accelerator program ends?</u></b><br>

    •Answer: After completion, startups typically present at a demo day and pursue seed or Series A funding. Many private accelerators continue to support startups through alumni networks and follow-on investment opportunities.
</p>

                        

  <p><u><b>12. What are the key benefits of joining a private accelerator?</u></b><br>

    •Answer: Key benefits include fast access to capital, high-quality mentorship, strong investor exposure, rapid growth acceleration, and increased credibility within the startup ecosystem.
</p>

                        

   <p><u><b>13. What are the risks or limitations of private accelerators?</u></b><br>

    •Answer: Risks include equity dilution, intense time commitment, pressure to grow quickly, and potential misalignment if the accelerator’s network or sector focus does not match the startup’s needs.
</p>

                        

 <p><u><b>14. How does a private accelerator compare to venture capital?</u></b><br>

    •Answer: Private accelerators invest earlier and smaller amounts than VCs and provide hands-on operational support. Venture capital typically invests later with larger checks and less day-to-day involvement.
</p>

                        

  <p><u><b>15. How can startups improve their chances of being accepted into a private accelerator?</u></b><br>

    •Answer: Startups should demonstrate strong teams, clear market opportunity, early traction, scalability, and a compelling growth narrative. Alignment with the accelerator’s sector focus significantly improves acceptance chances.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratorprivatetwelve(request):
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

    Capital Type: Private</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Private accelerators are best suited for pre-seed to early seed–stage startups, typically those with an MVP, early traction, or validated problem–solution fit. These programs focus on rapid growth, market entry, and investor readiness rather than idea validation.

    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Private accelerators strongly prefer C-Corporations, as these structures align with equity investment, future venture capital rounds, and scalable growth models. LLCs may be accepted in limited cases, but founders are often required to convert to a C-Corp before or during the program.

    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

Private accelerators usually accept startups with minimal prior funding, such as founder bootstrapping, grants, or small angel investments. Startups that have already raised large seed or Series A rounds are typically outside the accelerator’s target profile.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Prior non-dilutive funding is generally acceptable. However, existing equity investments are carefully reviewed to ensure that cap table complexity and dilution levels do not conflict with the accelerator’s equity requirements or future investor expectations.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Private accelerators typically provide initial seed capital ranging from $50,000 to $250,000, in exchange for equity. The primary value lies in access to follow-on venture capital, angel investors, and demo day exposure, enabling startups to raise larger rounds after graduation.

    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>

These accelerators align most closely with the pre-seed and seed funding stages. They help startups refine traction metrics, business models, and growth strategies in preparation for institutional fundraising.
    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>

Funding is usually delivered in a single upfront tranche at the start of the program. Some accelerators may provide additional incentives, prizes, or follow-on investments based on performance.
    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds are intended for growth-oriented activities, including:
<br>•	Product development and iteration
<br>•	Marketing and customer acquisition
<br>•	Hiring key early team members
<br>•	Core operational expenses
Use of funds for personal expenses or unrelated ventures is prohibited.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Risk is high, as startups must meet aggressive growth milestones within a short timeframe. Founders face equity dilution, performance pressure, and competitive program environments. Failure to secure follow-on funding remains a key risk.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is moderate to high, typically involving 5–10% equity dilution. While no debt repayment is required, the long-term cost depends on the company’s future valuation and growth success.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

Most private accelerators charge no upfront fees, but founders should budget for indirect costs such as legal restructuring, relocation, travel, and living expenses during the program.
    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The application and selection process usually takes 2–4 months. Once accepted, capital is typically disbursed immediately or within a few weeks, making private accelerators relatively fast sources of early-stage funding.

</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)