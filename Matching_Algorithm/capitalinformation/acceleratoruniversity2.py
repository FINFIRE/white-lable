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


def acceleratoruniversity(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Accelerator</b></u><br>

    Capital Type: University </center></p>

    <p><b><u>Introduction</u></b><br>

University Accelerators are ideal for startups seeking early-stage growth support within an academic ecosystem, combining structured mentorship, seed funding, and access to university resources, research expertise, and alumni networks. They are designed so that university-supported programs can help student-led, alumni-founded, or faculty-driven startups accelerate commercialization and prepare for external funding and market entry. {n} fits that definition. University accelerators have become increasingly prominent over the past decade as universities play a more active role in entrepreneurship and innovation ecosystems. For example, Stanford’s StartX has supported over 900 startups, which have collectively raised more than $9 billion in funding. MIT’s delta v Accelerator has helped hundreds of student-founded startups progress from idea stage to venture-backed companies. Oxford Foundry’s accelerator programs have supported dozens of university spin-outs and startups, contributing significantly to regional innovation and enterprise development. On average, university accelerator-backed startups receive between $10,000 and $150,000 in seed funding or grants, along with extensive mentorship, workspace, and investor exposure. While university accelerators provide strong credibility and foundational support, their fixed timelines, academic alignment, and eligibility requirements may limit flexibility for some ventures.
    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.University accelerators are structured, cohort-based programs operated by universities or affiliated institutions to support early-stage startups through intensive mentorship, training, and limited seed funding. These programs typically run for a fixed duration—often between 8 and 16 weeks—and focus on rapid business development, customer validation, and investment readiness. University accelerators leverage faculty expertise, research facilities, alumni networks, and institutional reputation to support innovation-driven ventures. Unlike private accelerators, university accelerators often provide non-dilutive funding or take minimal equity and prioritize education, research commercialization, and ecosystem development alongside financial outcomes. (Harvard Business Review, n.d.)

<br>



    <br>2.  The best type of companies to raise money through university accelerators are early-stage startups with a validated idea, prototype, or minimum viable product (MVP), particularly those founded by students, alumni, or faculty members. These startups often operate in knowledge-intensive sectors such as technology, health sciences, fintech, edtech, climate innovation, AI, and social enterprise. University accelerators are well-suited for ventures that benefit from academic research, technical expertise, or institutional credibility. Companies in the pre-seed to seed stage with strong innovation potential, committed founding teams, and a willingness to engage in structured learning environments tend to benefit most from these programs. (OECD, 2021)

<br>


    <br>3. University accelerators emerged in the early 2010s as an evolution of traditional university incubators, influenced by the success of private accelerators such as Y Combinator and Techstars. As universities sought faster commercialization of research and stronger engagement with startup ecosystems, accelerator-style programs were introduced to provide intensive, time-bound support. Institutions like Stanford, MIT, and Harvard pioneered these models, integrating entrepreneurship education with venture development. Over time, governments and development agencies recognized university accelerators as effective tools for innovation, job creation, and regional economic growth. Today, university accelerators are a key component of national and global innovation strategies. (World Bank, 2020)

<br>

    <br>4.While university accelerators offer valuable support, several risks and limitations should be considered. These programs are highly competitive, with limited cohort sizes and strict eligibility requirements, often restricted to university-affiliated founders. The fixed program duration and intensive schedule may be challenging for founders balancing academic or professional commitments. Funding amounts are usually modest compared to private accelerators or venture capital, potentially limiting scalability. Additionally, university administrative processes can slow decision-making, and intellectual property ownership may become complex when university resources or research are involved. (European Commission, 2022)

<br>

    <br>5. 
To raise capital through a university accelerator, a startup must typically apply through a competitive selection process involving written applications, pitch decks, and interviews. Applicants are evaluated based on innovation, scalability, team capability, and alignment with the university’s mission. Once accepted, startups participate in structured programming, including mentorship sessions, workshops, customer discovery, and pitch preparation. Seed funding—if offered—is usually provided as grants, stipends, or small equity investments. Programs often conclude with a demo day, where startups present to angel investors, venture capitalists, and industry partners. A strong pitch, clear traction, and demonstrated learning progress are essential for securing follow-on funding. (Startup Genome, n.d.)
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>Harvard Business Review. (n.d.). How startup accelerators work. <a href="https://hbr.org/2016/03/what-startup-accelerators-really-do?utm_.com ">https://hbr.org/2016/03/what-startup-accelerators-really-do?utm_.com </a>

<br>

    <br>OECD. (2021). Entrepreneurship, SMEs and innovation. <a href="https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/06/oecd-sme-and-entrepreneurship-outlook-2021_c4d635de-97a5bbfe-en.pdf ">https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/06/oecd-sme-and-entrepreneurship-outlook-2021_c4d635de-97a5bbfe-en.pdf</a>

<br>

    <br>World Bank. (2020). Building startup ecosystems. <a href=" https://openknowledge.worldbank.org/"> https://openknowledge.worldbank.org/</a>

<br>

    <br>European Commission. (2022). University entrepreneurship and accelerator programs. <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52022DC0332&utm_.com ">https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52022DC0332&utm_.com </a>

<br>

    <br>Startup Genome. (n.d.). Global accelerator ecosystem report. <a href="https://startupgenome.com/contents/report/gser-2025_4786.pdf ">https://startupgenome.com/contents/report/gser-2025_4786.pdf </a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	University Affiliation – Founder must be a student, alumnus, or faculty member
<br>•	Registered Business or Startup Project – Legal or pre-legal structure required
<br>•	Eligible Location – May need to operate within the university or regional ecosystem
<br>•	IP Ownership – Clear declaration of intellectual property rights
<br>•	Founder Eligibility – Legal age and authorization to participate
<br>•	No Academic or Legal Disputes – Clean disciplinary and legal record
<br>•	Compliance with University Policies – Academic, ethical, and conduct standards
<br>•	Participation Commitment – Mandatory attendance and milestone completion
<br>•	Fund Use Oversight – Compliance with reporting and spending rules



    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Proof of University Affiliation – Student ID, alumni letter, or faculty proof
<br>•	Startup Application Form – Accelerator-specific application
<br>•	Pitch Deck – Business model, product, market, team, and traction
<br>•	Business Plan or Lean Canvas – Strategy and revenue model
<br>•	MVP or Prototype Evidence – Demo, screenshots, or pilot results
<br>•	Founders’ Resumes/Bios – Academic and professional background
<br>•	IP Disclosure or Assignment – Ownership documentation
<br>•	Financial Projections – Funding needs and cost estimates
<br>•	Program Agreement – Signed participation and compliance documents


    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratoruniversityfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Accelerator<br>

    University</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is a university accelerator?</u></b><br>

    •Answer: A university accelerator is a time-bound startup program run or supported by a university that helps early-stage startups rapidly develop, validate, and scale their business. It combines academic support with industry mentorship, structured training, and limited funding or investment readiness support.
</p>

                            

     <p><u><b>2. How does a university accelerator differ from a university incubator?</u></b><br>

    •Answer: University accelerators are shorter, more intensive, and growth-oriented, focusing on rapid validation and commercialization. University incubators, in contrast, operate over longer periods and emphasize idea development, research, and foundational learning rather than fast scaling.
</p>


                            

    <p><u><b>3. What types of businesses are best suited for university accelerators?</u></b><br>

    •Answer: University accelerators are best suited for startups that already have a validated idea, prototype, or early traction. Student-led, faculty-led, and alumni startups in technology, innovation, or impact-driven sectors are particularly well-aligned.
</p>


                            

   <p><u><b>4. Do university accelerators provide funding?</u></b><br>

    •Answer: Some university accelerators provide small seed funding, grants, or stipends, while others focus on investment readiness rather than direct capital. Funding amounts are typically modest and may be non-dilutive or structured as equity, SAFE, or convertible notes.
</p>


                            

    <p><u><b>5. How quickly can startups access support after acceptance?</u></b><br>

    •Answer: Once accepted, startups usually begin the accelerator program immediately or within a few weeks. Access to mentorship, workshops, and university resources starts at the beginning of the program, with funding (if offered) provided early or upon milestone completion.
</p>


                            

   <p><u><b>6. What are the costs of participating in a university accelerator?</u></b><br>

    •Answer: Participation costs are generally low. Many university accelerators charge no fees due to institutional or government support. If funding is provided, equity dilution—if any—is usually lower than private accelerators.
</p>


                            

 <p><u><b>7. Do university accelerators take equity?</u></b><br>

    •Answer: Equity requirements vary. Some university accelerators take no equity, while others take a small equity stake (typically 2–7%) in exchange for funding, mentorship, and program access. Terms are usually founder-friendly.
</p>
                            

     <p><u><b>8. Can startups raise external funding while in a university accelerator?</u></b><br>

    •Answer: Yes, startups are encouraged to raise external funding. University accelerators often culminate in demo days, pitch events, or investor showcases, and typically place few restrictions on outside fundraising.
</p>

                            

   <p><u><b>9. What resources and support do university accelerators provide?</u></b><br>

    •Answer: Support includes structured mentorship, business model refinement, pitch training, access to faculty expertise, student talent, legal and IP guidance, co-working space, and networking with investors and industry partners.
</p>

                            

    <p><u><b>10. How long do university accelerator programs last?</u></b><br>

    •Answer: Programs usually last between 8 to 16 weeks. The fixed duration creates urgency and focus, helping startups achieve key milestones such as product validation, customer traction, or fundraising readiness.
</p>

                        

   <p><u><b>11. What happens after the accelerator program ends?</u></b><br>

    •Answer: After graduation, startups typically pursue seed funding, enter public or private accelerators, or transition into incubators for continued support. Many universities offer alumni networks, continued mentorship, and access to institutional partnerships.
</p>

                        

  <p><u><b>12. What are the risks of joining a university accelerator?</u></b><br>

    •Answer: Risks include time commitment, potential equity dilution, and limited funding size. Additionally, some programs may be academically focused and less connected to high-growth venture networks compared to private accelerators.
</p>

                        

   <p><u><b>13. How does a university accelerator compare to private accelerators or VC funding?</u></b><br>

    •Answer: University accelerators focus more on learning, mentorship, and founder development, while private accelerators and VCs emphasize rapid scaling and financial returns. University accelerators often offer lower equity dilution and stronger educational support.
</p>

                        

 <p><u><b>14. Who typically gets accepted into university accelerators?</u></b><br>

    •Answer: Accepted startups often include students, alumni, or faculty founders with a working prototype or early traction. Selection criteria emphasize innovation, scalability, team commitment, and alignment with the university’s mission or expertise.
</p>

                        

  <p><u><b>15. How can a startup increase its chances of being accepted into a university accelerator?</u></b><br>

    •Answer: Startups should demonstrate problem-solution fit, a committed founding team, early validation, and clear growth potential. Aligning the startup’s focus with the university’s strengths and showing readiness for rapid execution improves acceptance chances.
</p>
           
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def acceleratoruniversitytwelve(request):
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

    Capital Type: University</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

The ideal stage for a company to join a university accelerator is early-stage to early-revenue. These programs support startups that have moved beyond the idea or incubation phase and are focused on building a minimum viable product (MVP), validating market demand, and preparing for commercialization. University accelerators bridge the gap between academic incubation and market-driven growth.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

University accelerators are generally flexible regarding entity type. LLCs and private limited companies are commonly accepted, especially those formed by students, alumni, or faculty members. While C-Corps are not always mandatory, startups planning to raise external capital after the program are often encouraged to adopt investor-friendly structures.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

University accelerators typically prefer startups that have raised minimal prior funding. Small grants, personal savings, or incubator support are usually acceptable. Startups that have already raised large institutional rounds may be considered beyond the scope of university accelerators.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Capital raised from non-dilutive sources such as grants, competitions, or incubators generally does not restrict participation. However, prior venture capital or complex equity structures may reduce eligibility, as university accelerators focus on early-stage development and academic-to-market transition.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

University accelerators provide modest seed funding, typically ranging from $5,000 to $50,000, if funding is offered at all. The primary value lies in mentorship, structured programs, and investor readiness. The accelerator helps startups position themselves to raise larger seed or pre-Series A funding after completion.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
University accelerators align most closely with the pre-seed and early seed rounds. They are designed to help startups refine business models, strengthen traction, and prepare investor pitch materials rather than close large funding rounds during the program.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funding, when provided, is usually released in a single tranche or in small milestone-based disbursements tied to program participation, demo days, or performance benchmarks. Non-financial support is often continuous throughout the program duration.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds and resources from university accelerators are typically restricted to:
<br>•	Product and MVP development
<br>•	Market validation and pilot projects
<br>•	Customer discovery and marketing tests
<br>•	Legal, compliance, and incorporation expenses
<br>•	Limited operational and team costs
Personal use and unrelated expenses are strictly prohibited.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

The overall risk level is moderate. Financial risk is lower than private accelerators due to smaller equity requirements or non-dilutive funding. However, startups face execution risk, time commitment constraints, and potential delays caused by academic schedules or program structure.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

The cost of capital is generally low to moderate. Many university accelerators do not require equity, while some may take a small equity stake (1–5%). The trade-off mainly involves time commitment and compliance with academic or institutional guidelines rather than high financial cost.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

Upfront costs are minimal, often limited to application fees, documentation, or minor operational expenses. Access to university facilities, mentors, and infrastructure significantly reduces early-stage startup costs.
    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The selection process usually takes 1–3 months, depending on academic calendars and evaluation panels. Once accepted, access to funding (if applicable) and program resources begins quickly. Follow-on funding typically occurs after demo days or program completion, based on startup performance and investor interest.

</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)