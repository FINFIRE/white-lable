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


def grantsgovernment(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Grants 
</b></u><br>

    Capital Type:  Government </center></p>

    <p><b><u>Introduction</u></b><br>

Government grants are non-repayable funds provided by federal, state, or local governments to support businesses, non-profits, or research initiatives. These grants are designed to stimulate economic development, innovation, social programs, and public services. {n} fits that definition. For example, in 2023, the U.S. Small Business Administration awarded over $1 billion in grants to support innovation and small business growth.¹ Similarly, the European Union’s Horizon Europe program allocated €95.5 billion in funding for research and innovation projects from 2021–2027.² Government grants provide recipients with resources to implement projects without creating debt, making them an attractive funding option for early-stage ventures and socially impactful initiatives.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>

<br>1.	Government grants are financial awards provided by central or federal governments to businesses, startups, research institutions, or organizations for clearly defined purposes aligned with national economic, social, or technological objectives. These funds do not require repayment, provided recipients comply with the grant’s terms and conditions. Government grants are commonly used to support innovation, research and development (R&D), employment generation, sustainability initiatives, export promotion, and regional development. Unlike loans or equity financing, government grants do not create ownership claims or repayment obligations; however, they impose strict accountability through monitoring, reporting, and auditing mechanisms to ensure responsible use of public funds (OECD, n.d.).



    <br>

<br>2.	Government grants are best suited for early-stage startups, small and medium-sized enterprises, and innovation-driven companies that operate in priority sectors identified by national governments. These sectors often include renewable energy, agriculture, manufacturing, biotechnology, health technology, information technology, education, and social enterprise. Companies that demonstrate strong innovation potential, measurable public or social impact, and alignment with national development goals tend to be the most competitive applicants. Government grants are particularly valuable for firms that face difficulties accessing private capital due to high uncertainty, long development cycles, or significant upfront investment requirements (World Bank, 2021).


    <br>

<br>3.	Government grant programs expanded significantly during the 20th century as states assumed a greater role in economic planning, industrial policy, and innovation support. Following major economic disruptions such as the Great Depression, post-war reconstruction, the 2008 global financial crisis, and the COVID-19 pandemic, governments increasingly relied on grants to stabilize economies and encourage business formation. In recent decades, government grants have become central components of national innovation systems, supporting research commercialization, startup ecosystems, and technology transfer initiatives (European Commission, 2022).⁴

    <br>

<br>4.	Despite their advantages, government grants involve several risks and limitations. Application processes are often complex, time-consuming, and highly competitive, with low acceptance rates. Funding is usually restricted to specific activities, reducing operational flexibility. Grant recipients are subject to extensive reporting, monitoring, and auditing requirements, and failure to comply may result in funding withdrawal or repayment obligations. In addition, grant availability can fluctuate based on political priorities, fiscal constraints, or policy changes, creating uncertainty for long-term business planning (KPMG, 2022).

    <br>

    <br>5.	To raise capital through government grants, a company must first identify suitable grant programs and confirm eligibility based on sector, business size, location, and project objectives. The application process typically involves submission of a detailed proposal outlining the business model, project scope, budget, timeline, and expected economic or social outcomes. Applicants may also be required to demonstrate financial stability, technical capability, and compliance with tax and regulatory obligations. Successful recipients must enter into a formal grant agreement and comply with milestone-based reporting, performance evaluation, and audit requirements throughout the grant period (OECD, 2020).
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>OECD. (n.d.). Public grants and innovation policy. <a href=" https://www.oecd.org/innovation "> https://www.oecd.org/innovation </a>

<br>

     <br>World Bank. (2021). Government support for SMEs and startups. <a href=" https://www.worldbank.org"> https://www.worldbank.org</a>

<br>

   <br>European Commission. (2022). State aid and business grants. <a href=" https://commission.europa.eu"> https://commission.europa.eu</a>

<br>

   <br>KPMG. (2022). Managing compliance and risk in government grants. <a href=" https://home.kpmg"> https://home.kpmg</a>

<br>

   <br>OECD. (2020). Public funding and entrepreneurship. <a href=" https://www.oecd.org"> https://www.oecd.org</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Registered business or non-profit organization
<br>•	Compliance with tax and legal regulations
<br>•	Project aligned with grant objectives
<br>•	Proper documentation of project plan, budget, and team
<br>•	Ability to meet reporting and audit requirements




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Business registration certificate or proof of non-profit status
<br>•	Project proposal and detailed plan
<br>•	Budget and financial projections
<br>•	Team bios and qualifications
<br>•	Past performance metrics (if applicable)
<br>•	Compliance and audit documentation
<br>•	Letters of support or partnership agreements




    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantsgovernmentfaq(request):
    introduction = mark_safe("""<p><b><center>Capital Market: Grants<br>

    Government</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What are government grants?</u></b><br>

    •Answer: Government grants are non-repayable funds provided by federal, state, or local government agencies to support businesses, startups, research projects, or social enterprises. They aim to stimulate innovation, economic growth, employment, and social development.
</p>

                            

     <p><u><b>2. How do government grants differ from loans or equity financing?</u></b><br>

    •Answer: Government grants do not require repayment and do not involve giving up equity. Unlike loans, there is no interest, and unlike private investment, the business retains full ownership and control.
</p>


                            

    <p><u><b>3. What types of businesses are eligible for government grants?</u></b><br>

    •Answer: Eligibility varies by program but often includes startups, small and medium enterprises (SMEs), research and development firms, social enterprises, and businesses aligned with government priorities such as sustainability, technology, healthcare, and economic development.
</p>


                            

   <p><u><b>4. How much funding can businesses typically receive?</u></b><br>

    •Answer: Funding amounts vary widely depending on the grant program. Some small business grants range from a few thousand dollars to several hundred thousand, while research or innovation grants can reach millions for large-scale projects.
</p>


                            

    <p><u><b>5. How quickly can businesses access government grant funds?</u></b><br>

    •Answer: Access timelines depend on the grant program and evaluation process. Disbursement may take weeks to months after application approval, with some programs releasing funds in stages tied to project milestones.
</p>


                            

   <p><u><b>6. Are there restrictions on how grant funds can be used?</u></b><br>

    •Answer: Yes. Government grants usually have strict guidelines on fund usage. Funds may be restricted to specific purposes such as R&D, equipment purchase, hiring, training, or market expansion, and cannot be used for unrelated expenses.
</p>


                            

 <p><u><b>7. Do government grants require matching funds?</u></b><br>

    •Answer: Some programs require the business to contribute matching funds (cash or in-kind), while others provide full funding. The requirement depends on the grant’s objectives and rules.
</p>
                            

     <p><u><b>8. Can pre-revenue startups apply for government grants?</u></b><br>

    •Answer: Yes. Many government grants target early-stage ventures, especially for innovation, research, or social impact projects. Applicants must demonstrate a feasible plan and alignment with program goals.
</p>

                            

   <p><u><b>9. Are there reporting and compliance requirements?</u></b><br>

    •Answer: Yes. Recipients must provide progress reports, financial statements, and performance metrics to ensure proper use of funds. Non-compliance can lead to penalties or grant recovery.
</p>

                            

    <p><u><b>10. Can government grants be combined with other funding sources?</u></b><br>

    •Answer: Yes. Government grants can be combined with loans, private investment, accelerators, or incubators, provided grant conditions are met and conflicts of interest are avoided.
</p>

                        

   <p><u><b>11. What are the key benefits of government grants?</u></b><br>

    •Answer: Benefits include non-dilutive funding, reduced financial risk, credibility, and alignment with government programs promoting growth, innovation, and social impact.
</p>

                        

  <p><u><b>12. What are the limitations or risks of government grants?</u></b><br>

    •Answer: Limitations include competitive application processes, restricted fund usage, administrative reporting requirements, and longer disbursement timelines compared to private capital.
</p>

                        

   <p><u><b>13. How do government grants compare to municipal grants?</u></b><br>

    •Answer: Government grants are usually larger in scale, broader in eligibility, and may be targeted nationally or regionally. Municipal grants are smaller, more localized, and focus on local development priorities.
</p>

                        

 <p><u><b>14. What types of projects are commonly funded?</u></b><br>

    •Answer: Projects often funded include research and development, innovation and technology adoption, sustainability initiatives, community development, workforce training, and social enterprises.
</p>

                        

  <p><u><b>15. How can businesses improve their chances of securing government grants?</u></b><br>

    •Answer: Businesses should align applications with grant objectives, provide a detailed budget, demonstrate impact and feasibility, maintain proper financial records, and clearly show how funds will be used effectively.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantsgovernmenttwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Grants</b></u><br>

    Capital Type: Government</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

Government grants are suitable for idea-stage to early-growth businesses, including startups, SMEs, and innovation-driven projects. Grants target initiatives with economic, technological, social, or environmental impact aligned with national priorities.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Eligible entities generally include formally registered businesses, such as sole proprietorships, partnerships, LLCs, and corporations. Some programs may also target research institutions, non-profits, or public-private collaborations.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Government grants typically do not require prior funding, but some programs may require matching funds or co-financing to demonstrate commitment and ensure efficient use of public resources.

    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Grants operate outside equity or debt markets. Previous equity or debt financing usually does not affect eligibility, as grants are non-dilutive and non-repayable.

    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

Grant amounts vary widely, from small seed grants to multi-million project funding. They are intended to support specific projects, research, or innovation initiatives, rather than general business expansion.
    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>

Grants are not tied to traditional fundraising rounds. Funding is allocated per project or program cycle and often depends on national budget allocations and policy priorities.
    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>

Funds are often disbursed in phased tranches, such as:
<br>•	Initial approval advance
<br>•	Milestone-based disbursements
<br>•	Final payment upon completion and reporting
This ensures accountability and proper use of funds.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Grant funds must be used strictly for approved purposes, which may include:
<br>•	Research and development
<br>•	Innovation and technology adoption
<br>•	Workforce development and training
<br>•	Sustainability and social impact initiatives
Funds cannot be used for personal expenses or unrelated activities.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Financial risk is low since grants are non-repayable. However, compliance risk is high, including reporting requirements, audits, and potential clawback of funds if conditions are not met.
    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is zero, as grants do not require repayment or equity dilution. The indirect cost is administrative effort and adherence to grant conditions.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are minimal, usually related to proposal preparation, documentation, and compliance setup. There are no fees for accessing grant funds directly.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Government grants often have longer timelines, typically 3–12 months from application to disbursement, depending on program complexity, budget cycles, and evaluation procedures.
</p>"""

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)