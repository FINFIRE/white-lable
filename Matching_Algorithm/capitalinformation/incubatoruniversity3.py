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


def incubatoruniversity(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Incubator</b></u><br>

    Capital Type: University </center></p>

    <p><b><u>Introduction</u></b><br>

University incubators are institution-backed programs designed to support early-stage startups, student entrepreneurs, and faculty-led ventures by providing infrastructure, mentorship, academic expertise, and access to research and innovation ecosystems. {n} fits that definition. These incubators operate within universities or affiliated institutions and aim to commercialize research, promote entrepreneurship, and encourage knowledge transfer from academia to industry. University incubators typically offer low-cost workspace, technical guidance, access to laboratories, faculty mentors, and connections to investors and industry partners. According to the National Business Incubation Association (NBIA), startups supported by university incubators have a survival rate exceeding 85% after five years. Globally recognized examples include MIT’s Martin Trust Center for Entrepreneurship, Stanford StartX, and Oxford University Innovation. While university incubators offer strong foundational support, they often focus more on learning, experimentation, and long-term development rather than rapid scaling or immediate capital deployment.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>
1.University incubators are entrepreneurship support programs established within or in partnership with higher education institutions to nurture early-stage startups. These incubators provide non-dilutive support such as mentoring, training, office space, research facilities, and access to academic networks. Funding, if provided, is usually limited and comes in the form of grants, stipends, or competition-based seed funding rather than direct investment. University incubators prioritize innovation, research commercialization, and student or faculty entrepreneurship. Unlike accelerators, incubators typically have flexible timelines and focus on long-term venture development rather than rapid growth. (OECD, n.d.)
<br>



    <br>
2.University incubators are best suited for idea-stage to early-stage startups, particularly those founded by students, researchers, or academic professionals. These programs are ideal for ventures based on research, innovation, deep tech, health sciences, engineering, sustainability, education technology, and social enterprises. Startups that require technical validation, prototyping, or academic expertise benefit significantly from university incubators. They are also suitable for founders who may lack business experience but have strong technical or theoretical knowledge. Companies that value learning, mentorship, and experimentation over immediate commercialization gain the most from university incubator environments. (World Bank, 2020)
<br>


    <br>
3.University incubators emerged in the late 20th century as universities began to recognize their role in economic development and innovation ecosystems. One of the earliest examples is the Batavia Industrial Center (1959), which influenced later academic incubation models. During the 1980s and 1990s, universities in the United States and Europe increasingly established incubators to commercialize academic research and encourage faculty-led entrepreneurship. The success of Silicon Valley, driven largely by Stanford University spin-offs, further accelerated the adoption of university incubators worldwide. In recent decades, governments and international organizations have promoted university incubators as tools for job creation, innovation, and regional development, particularly in emerging economies. (NBIA, 2021)

<br>

    <br>
4.While university incubators provide valuable support, they also present certain limitations. Funding availability is often limited compared to private accelerators or venture capital, which may restrict growth opportunities. Decision-making processes can be slower due to academic bureaucracy and administrative structures. Some incubators prioritize research output or academic objectives over market viability, which may delay commercialization. Additionally, participation may be restricted to students, alumni, or faculty, limiting access for external entrepreneurs. Intellectual property (IP) ownership can also be complex, particularly when university resources or research are involved. (European Commission, 2022)

<br>

    <br>
5. To raise capital through a university incubator, founders typically apply through a competitive selection process that evaluates innovation, feasibility, academic alignment, and societal impact. Applicants often need to present a concept note, business plan, or research proposal. Once accepted, startups gain access to mentoring, workshops, and institutional resources. Funding, if available, is usually provided through grants, business plan competitions, innovation funds, or government-supported university programs. Startups are expected to actively participate in training sessions, mentoring meetings, and progress reviews. Many founders use university incubators as a pre-funding stage, later transitioning to accelerators, angel investors, or venture capital once market validation is achieved. (UNESCO, n.d.)    </p>

                            

    <p><u><b>References</u></b><br>

    <br>OECD. (n.d.). University entrepreneurship and incubation. <a href=" https://www.oecd.org"> https://www.oecd.org</a>

<br>

    <br>World Bank. (2020). Innovation and entrepreneurship ecosystems. <a href=" https://www.worldbank.org"> https://www.worldbank.org</a>

<br>

    <br>National Business Incubation Association (NBIA). (2021). Impact of university incubators. <a href=" https://inbia.org"> https://inbia.org</a>

<br>

    <br>European Commission. (2022). University-based innovation hubs. <a href=" https://commission.europa.eu"> https://commission.europa.eu</a>

<br>

    <br>UNESCO. (n.d.). Higher education and innovation. <a href=" https://www.unesco.org"> https://www.unesco.org</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•Affiliation Requirement – Founder must be a student, alumnus, or faculty member (in most cases)
<br>•	Registered Business or Project – Startup or venture must be formally documented
<br>•	IP Disclosure – Declaration of intellectual property ownership
<br>•	Compliance with University Policies – Must follow academic and ethical guidelines
<br>•	Founder Eligibility – Legal age and enrollment or employment verification
<br>•	No Academic Misconduct – Clean disciplinary record
<br>•	Research Approval – Required for research-based ventures
<br>•	Use of Facilities Agreement – Acceptance of incubator terms
<br>•	Reporting Obligations – Regular progress and impact reports




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•   Proof of University Affiliation – Student ID, enrollment letter, or faculty appointment
<br>•	Concept Note or Research Proposal – Description of idea or innovation
<br>•	Business Plan or Lean Canvas – Business model and strategy
<br>•	Pitch Deck – Overview of solution, market, and team
<br>•	IP Disclosure Form – Ownership and usage rights
<br>•	Founders’ CVs – Academic and professional background
<br>•	Project Timeline – Development milestones
<br>•	Financial Projections – Estimated costs and funding needs
<br>•	Ethics Approval – If applicable for research-based startups

    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatoruniversityfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Incubator<br>

    University</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is a university incubator?</u></b><br>

    •Answer: A university incubator is a startup support program run or sponsored by a university to help early-stage ventures develop ideas into viable businesses. These incubators focus on long-term business development by providing mentorship, academic expertise, research access, infrastructure, and limited funding support.
</p>

                            

     <p><u><b>2. How does a university incubator differ from an accelerator?</u></b><br>

    •Answer: University incubators operate over a longer time horizon and focus on idea validation, research, and early development rather than rapid scaling. Unlike accelerators, incubators usually do not require equity and emphasize education, experimentation, and foundational business building.
</p>


                            

    <p><u><b>3. What types of businesses are best suited for university incubators?</u></b><br>

    •Answer: University incubators are best suited for idea-stage to early-stage startups, particularly those based on research, innovation, technology transfer, or social impact. Student-led startups, faculty ventures, and research-driven enterprises align especially well with university incubators.
</p>


                            

   <p><u><b>4. Do university incubators provide funding?</u></b><br>

    •Answer: Most university incubators provide limited or no direct cash funding. Instead, they offer non-dilutive support such as grants, stipends, prototype funding, or access to university resources. Some programs may offer small seed funds or help startups connect with external funding sources.
</p>


                            

    <p><u><b>5. How quickly can a startup access support from a university incubator?</u></b><br>

    •Answer: Once accepted, startups can usually access incubator resources immediately or within a few weeks. Since funding is not the primary focus, access to mentorship, workspace, and academic support begins early in the program.
</p>


                            

   <p><u><b>6. What are the costs of participating in a university incubator?</u></b><br>

    •Answer: Participation costs are generally very low or free. Many university incubators are subsidized by the institution or government programs. Some may charge nominal membership fees, but equity dilution is uncommon.
</p>


                            

 <p><u><b>7. Do university incubators require equity in exchange for support?</u></b><br>

    •Answer: Most university incubators do not take equity. Their primary objective is education, innovation, and commercialization of ideas rather than financial returns. However, exceptions may exist for incubators linked to university-affiliated investment funds.
</p>
                            

     <p><u><b>8. Can a startup raise capital while in a university incubator?</u></b><br>

    •Answer: Yes, startups are encouraged to raise external funding while in an incubator. University incubators often facilitate introductions to angel investors, grant programs, venture funds, and public accelerators, without restricting external fundraising.
</p>

                            

   <p><u><b>9. What resources and support do university incubators provide?</u></b><br>

    •Answer: University incubators typically provide mentorship from faculty and industry experts, access to research labs, libraries, student talent, office or co-working space, workshops, and business development support. Some also offer legal, IP, and commercialization guidance.
</p>

                            

    <p><u><b>10. How long do startups usually stay in a university incubator?</u></b><br>

    •Answer: Incubation periods vary widely, ranging from 6 months to several years. The flexible timeline allows startups to mature at a sustainable pace, especially those developing complex or research-intensive products.
</p>

                        

   <p><u><b>11. What happens after a startup exits a university incubator?</u></b><br>

    •Answer: After graduation, startups often move on to accelerators, angel funding, or early-stage venture capital. Universities may continue to provide alumni support, networking opportunities, and access to partnerships or research collaborations.
</p>

                        

  <p><u><b>12. Are there any risks associated with university incubators?</u></b><br>

    •Answer: Risks include slower growth due to the non-competitive pace, limited access to large amounts of capital, and potential misalignment if the incubator is more academically focused than market-driven. Startups seeking rapid scaling may outgrow incubators quickly.
</p>

                        

   <p><u><b>13. How does a university incubator compare to angel investors or venture capital?</u></b><br>

    •Answer: University incubators focus on capacity building rather than financial returns. Unlike angels or VCs, incubators provide structured learning, mentorship, and infrastructure without pressure for fast exits or high growth, making them ideal for early exploration stages.
</p>

                        

 <p><u><b>14. Who typically gets accepted into university incubators?</u></b><br>

    •Answer: Accepted startups often include students, faculty members, researchers, or alumni with innovative ideas. Selection criteria usually emphasize problem-solution fit, innovation potential, feasibility, and alignment with the university’s research or social mission.
</p>

                        

  <p><u><b>15. How can a startup increase its chances of being accepted into a university incubator?</u></b><br>

    •Answer: Startups can improve acceptance chances by presenting a clear problem statement, demonstrating innovation or research depth, showing commitment from the founding team, and aligning their idea with the university’s strengths or focus areas.
</p>
    """)

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatoruniversitytwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Incubator</b></u><br>

    Capital Type: University</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
University incubators are best suited for businesses at the idea stage to early-revenue stage. They primarily support student-led or research-based startups that are still validating concepts, developing prototypes, or conducting pilot testing. These incubators focus on learning, experimentation, and early commercialization rather than rapid scaling.

    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

University incubators are generally flexible regarding entity type. Sole proprietorships, partnerships, early-stage LLCs, and even unregistered project-based startups are often eligible. Formal incorporation may not be mandatory at entry, but startups are usually encouraged to register as an LLC or private limited company as they progress.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Most university incubators do not require prior funding. In fact, they often prefer startups with minimal or no external capital, as their goal is to support founders who lack access to traditional financing. Pre-existing grants or small personal investments are typically acceptable.

    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
University incubators are non-market-based and operate outside traditional capital markets. They are funded by universities, governments, or development partners. Previous venture capital or large equity investments may reduce eligibility, as incubators focus on early academic and innovation-driven ideas.

    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

University incubators typically provide limited direct capital, often ranging from seed grants, stipends, or prototype funding. The primary value lies in non-financial support, including mentorship, labs, infrastructure, and credibility. They prepare startups to raise larger funding later from accelerators, angels, or grants.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Incubator participation aligns most closely with the pre-seed or ideation phase. Unlike accelerators, incubators are not designed around formal funding rounds. Instead, they support long-term idea development before the startup is ready for structured fundraising.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funding, if provided, is usually released in small tranches tied to milestones, such as prototype completion, research validation, or demo day presentations. Some incubators offer non-cash support instead of monetary tranches.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds and resources from university incubators are typically restricted to:
<br>•	Research and development
<br>•	Prototype and MVP development
<br>•	Testing and validation
<br>•	Academic–industry collaboration
<br>•	Early operational expenses

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>
The financial risk for startups in a university incubator is relatively low, as funding is often non-dilutive and support-based. However, there is execution risk related to academic timelines, limited market exposure, and slower commercialization compared to private accelerators.

    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

The cost of capital is generally low to zero, as most university incubators do not take equity or charge fees. In some cases, a small equity stake or intellectual property sharing agreement may apply, particularly for research-based innovations.
    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

Upfront costs are minimal, often limited to registration fees, documentation, or participation commitments. Access to university infrastructure significantly reduces operational costs for early-stage startups.
    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The selection process may take 1–3 months, depending on academic calendars and evaluation committees. Once accepted, access to resources and limited funding is usually provided quickly, though disbursements may align with academic or grant cycles.

</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)