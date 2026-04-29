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


def incubatorpublic(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Incubator</b></u><br>

    Capital Type: Public  </center></p>

    <p><b><u>Introduction</u></b><br>

Public incubators are government-supported or publicly funded programs designed to nurture early-stage startups by providing long-term support, infrastructure, mentorship, and access to public innovation resources. These incubators focus on helping startups develop ideas, validate business models, and gradually move toward commercialization, particularly in sectors aligned with public policy objectives such as employment generation, innovation, and regional development. {n} fits that definition. Public incubators have been widely used across the world as tools for economic development and entrepreneurship promotion. For example, the European Business and Innovation Centre Network (EBN) has supported thousands of startups across Europe through publicly backed incubators. Similarly, India’s Atal Incubation Centres (AICs) have supported hundreds of startups since their launch under the Atal Innovation Mission. Public incubators typically offer subsidized workspace, mentoring, training, and access to grants rather than rapid scaling or equity-based funding. While public incubators provide stability and long-term support, slower growth pace and administrative requirements may limit flexibility for some startups.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1. Public incubators are incubation programs established and funded by governments, public agencies, or public–private partnerships to support early-stage startups and entrepreneurs. They provide non-dilutive support such as subsidized workspace, mentoring, technical assistance, business development services, and access to government grants or innovation schemes. Unlike accelerators, public incubators usually operate with flexible timelines and focus on long-term venture development rather than rapid growth. Their primary objectives include innovation promotion, job creation, and regional economic development rather than immediate financial returns. (OECD, n.d.)

<br>



    <br>2.  Public incubators are best suited for idea-stage to early-stage startups, micro-enterprises, and innovation-driven ventures that require foundational support rather than immediate scaling. These include startups in sectors such as agriculture, manufacturing, clean energy, healthcare, education, ICT, and social enterprises. Public incubators are particularly beneficial for startups operating in underserved regions or industries where private investment is limited. Entrepreneurs with innovative ideas, limited capital, and long-term development objectives tend to benefit most from public incubation support. (World Bank, 2020)

<br>


    <br>3. Public incubators emerged in the late 1950s, with the Batavia Industrial Center in the United States often cited as the first formal business incubator. The model expanded significantly during the 1980s and 1990s as governments recognized entrepreneurship as a driver of innovation, employment, and regional development. Over time, public incubators became central components of national innovation systems, particularly in developing and transition economies. In recent years, public incubation has expanded globally, with increased emphasis on technology, sustainability, and social innovation. (INBIA, 2021)

<br>

    <br>4. Despite their advantages, public incubators have several limitations. Growth may be slower due to the absence of strict timelines and limited access to large-scale funding. Administrative and reporting requirements may be bureaucratic, reducing operational flexibility. The quality of mentorship and facilities can vary depending on government capacity and funding availability. In some cases, prolonged dependence on public support may delay startups’ transition to competitive, market-based financing. (European Commission, 2022)

<br>

    <br>5. To access support through a public incubator, startups typically apply through a formal selection process assessing innovation, feasibility, economic or social impact, and regional relevance. Applicants may be required to submit a concept note, business plan, or project proposal. Once selected, startups receive incubation services such as workspace, mentoring, training, and access to public funding schemes. Financial support is usually provided in the form of grants, subsidies, or innovation vouchers. Startups are required to meet progress milestones and comply with monitoring and reporting requirements set by the incubator or funding authority. (UNIDO, n.d.)
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>OECD. (n.d.). Incubators and accelerators. <a href="https://www.oecd.org/innovation/incubators-and-accelerators.htm ">https://www.oecd.org/innovation/incubators-and-accelerators.htm </a>

<br>

     <br>World Bank. (2020). Entrepreneurship and innovation ecosystems. <a href="https://www.worldbank.org/en/topic/entrepreneurship ">https://www.worldbank.org/en/topic/entrepreneurship </a>

<br>

   <br>International Business Innovation Association (INBIA). (2021). History of business incubation. <a href="https://inbia.org/resources/business-incubation-history/ ">https://inbia.org/resources/business-incubation-history/ </a>

<br>

   <br>European Commission. (2022). Innovation and startup policy. <a href="https://commission.europa.eu/strategy-and-policy/policies/innovation-and-research_en ">https://commission.europa.eu/strategy-and-policy/policies/innovation-and-research_en </a>

<br>

   <br>UNIDO. (n.d.). Entrepreneurship and innovation. <a href="https://www.unido.org/our-focus/advancing-economic-competitiveness/entrepreneurship-and-innovation ">https://www.unido.org/our-focus/advancing-economic-competitiveness/entrepreneurship-and-innovation </a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Registered Business or Approved Project
<br>•	Eligible Location – Must operate within the public incubator’s jurisdiction
<br>•	Licenses & Regulatory Compliance
<br>•	No Legal Disputes or Violations
<br>•	Founder Eligibility – Legal age and authorization
<br>•	IP Ownership Disclosure
<br>•	Compliance with Public Policies
<br>•	Reporting and Monitoring Obligations




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Certificate of Incorporation or Project Approval Letter
<br>•	Business License (if applicable)
<br>•	Concept Note or Business Plan
<br>•	Pitch Deck
<br>•	Founders’ CVs / Profiles
<br>•	IP Ownership or Disclosure Documents
<br>•	Financial Projections or Budget Plan
<br>•	Incubation Agreement
<br>•	Progress and Impact Reports
    </p> 
    """)
    introduction = mark_safe(introduction.format(n=name))



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatorpublicfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Incubator<br>

    Public </center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is a public incubator?</u></b><br>

    •Answer: A public incubator is a startup support program funded or operated by government bodies, public institutions, or non-profit organizations. Its main purpose is to nurture early-stage ventures by providing long-term guidance, infrastructure, and capacity-building support rather than focusing on rapid growth or financial returns.
</p>

                            

     <p><u><b>2. How does a public incubator differ from a public accelerator?</u></b><br>

    •Answer: Public incubators support startups over a longer and more flexible period, concentrating on idea hudevelopment, research, and business foundation. Public accelerators, in contrast, are time-bound programs designed to fast-track commercialization and early market entry.
</p>


                            

    <p><u><b>3. What stage of startups are best suited for a public incubator?</u></b><br>

    •Answer: Public incubators are best suited for idea-stage and very early-stage startups, including pre-revenue businesses that are still validating their concepts, technologies, or target markets.
</p>


                            

   <p><u><b>4. Do public incubators provide funding?</u></b><br>

    •Answer: Public incubators generally provide little to no direct investment capital. Support is often delivered through non-dilutive means such as grants, stipends, prototype funding, subsidized facilities, or access to public resources.
</p>


                            

    <p><u><b>5. How quickly can startups access incubator support after acceptance?</u></b><br>

    •Answer: Once accepted, startups usually gain immediate access to workspace, mentorship, and training programs. Any financial assistance, if available, is typically provided on a milestone or needs-based basis.
</p>


                            

   <p><u><b>6. What are the costs of participating in a public incubator?</u></b><br>

    •Answer: Participation costs are minimal or free, as public incubators are commonly subsidized by governments or donor organizations. Application or membership fees, if charged, are usually nominal.
</p>


                            

 <p><u><b>7. Do public incubators require equity from startups?</u></b><br>

    •Answer: Most public incubators do not take equity. Their objective is to promote entrepreneurship and innovation rather than generate investment returns. Equity requirements are rare and usually linked to separate investment vehicles.
</p>
                            

     <p><u><b>8. Can startups raise external funding while in a public incubator?</u></b><br>

    •Answer: Yes. Startups are encouraged to pursue external funding, including grants, angel investment, or accelerator programs. Public incubators often assist by improving investment readiness and making ecosystem introductions.
</p>

                            

   <p><u><b>9. What types of support do public incubators provide?</u></b><br>

    •Answer: Public incubators typically provide mentorship, business development training, shared office or lab space, regulatory and compliance guidance, access to research institutions, and networking with public and private stakeholders.
</p>

                            

    <p><u><b>10. How long do startups typically remain in a public incubator?</u></b><br>

    •Answer: Incubation periods are flexible and may range from several months to multiple years, depending on startup progress, sector complexity, and incubator policies.
</p>

                        

   <p><u><b>11. What happens after a startup exits a public incubator?</u></b><br>

    •Answer: After graduation, startups often move into public or private accelerators, seek seed funding, enter the market, or continue independently. Many public incubators maintain alumni support and ecosystem connections.
</p>

                        

  <p><u><b>12. What are the key benefits of joining a public incubator?</u></b><br>

    •Answer: Key benefits include low financial risk, no equity dilution, long-term mentorship, access to public infrastructure, and credibility within the startup ecosystem.
</p>

                        

   <p><u><b>13. What are the limitations or risks of public incubators?</u></b><br>

    •Answer: Limitations may include slower growth, limited direct funding, administrative processes, and fewer immediate investor connections compared to private accelerators or VCs.
</p>

                        

 <p><u><b>14. How does a public incubator compare to private incubators or investors?</u></b><br>

    •Answer: Public incubators emphasize learning, inclusion, and ecosystem development, while private incubators and investors focus on returns and scalability. Public incubators are typically more accessible at the earliest startup stages.
</p>

                        

  <p><u><b>15. How can startups improve their chances of acceptance into a public incubator?</u></b><br>

    •Answer: Startups should present a clearly defined problem, demonstrate innovation or social impact, show founder commitment, and align with the incubator’s public mission or priority sectors.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def incubatorpublictwelve(request):
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

    Capital Type: Public</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Public incubators are most suitable for idea-stage to very early-stage startups, including concept development, feasibility studies, and early prototypes. The focus is on nurturing ideas and building foundations rather than rapid scaling or commercialization.

    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Public incubators are highly flexible in terms of legal structure. They commonly accept individual founders, unregistered ventures, sole proprietorships, partnerships, and early-stage LLCs or private limited companies. Formal incorporation is often encouraged during the incubation period but is not always required at entry.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

Public incubators generally prefer startups with little or no prior funding. Bootstrapped projects, personal savings, or small grants are acceptable. Startups that have already raised substantial private or venture capital are often considered beyond the incubator’s target stage.
    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

These incubators operate outside traditional capital markets. Prior non-dilutive funding (government grants, academic support, competitions) is usually permitted. Significant equity-based funding may reduce eligibility, as public incubators focus on early capability building rather than investor-driven growth.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

Public incubators typically provide limited direct funding, if any. Support may come as small seed grants, stipends, or in-kind resources. Their main objective is to prepare startups for future accelerators, investors, or development programs rather than to fund large capital raises.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>

Public incubators align with the pre-pre-seed or ideation phase. They are not linked to formal funding rounds such as seed or Series A and instead support startups before structured fundraising begins.
    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Any financial support is usually released in small, milestone-based tranches, such as prototype completion or progress reviews. Many public incubators provide support entirely in non-cash forms like workspace, labs, or mentorship.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds and resources are restricted to:
<br>•	Research and proof-of-concept development
<br>•	Prototype and MVP creation
<br>•	Early operational setup
<br>•	Market testing and validation
<br>•	Training and capacity building
Personal use or unrelated expenses are not permitted.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

The financial risk to startups is low, as public incubators are mostly non-dilutive. However, startups face risks related to slow decision-making, administrative procedures, and potential delays due to public-sector governance.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is generally very low or zero. Most public incubators do not take equity. Instead, the “cost” comes in the form of compliance requirements, reporting obligations, and adherence to public policy objectives.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are minimal. Application fees, if charged, are usually nominal. Access to subsidized infrastructure and public resources significantly reduces early-stage startup expenses.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The application and selection process may take 1–4 months, depending on government procedures. Once accepted, access to facilities and mentorship is usually immediate, while any grant disbursement may follow administrative approval timelines.
</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)