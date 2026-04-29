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


def grantsstateagencies(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""<p><center><b><u>Definition of Capital Market: Grants</b></u><br>

    Capital Type: State Agencies </center></p>

    <p><b><u>Introduction</u></b><br>

State Agency Grants are ideal for companies seeking early-stage support, including non-dilutive funding, technical assistance, and access to state-specific resources and industry clusters. They are designed so that government-supported programs can help privately held startups and established small businesses grow, stimulate local economies, and prepare for further commercialization. {n} fits that definition. State agency grants have been a vital economic development tool for decades. For example, in 2023, the California Energy Commission (CEC) awarded over $1 billion in grants to accelerate clean energy innovation and infrastructure. The Texas Enterprise Fund has committed more than $600 million since its inception to attract and grow businesses that create high-paying jobs. In Massachusetts, MassLifeSciences has provided hundreds of millions in grants and tax incentives to solidify the state’s position as a global leader in biotechnology. On average, state agency grants recipients gain access to between **$50,000 and $500,000** in funding, often accompanied by specialized state-funded laboratory access or workforce training subsidies. While state agency grants offer significant non-dilutive capital, the rigorous reporting requirements, local residency mandates, and alignment with specific state political or economic goals can influence the strategic direction of a company.    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1.	State Agency Grants are government-funded financial awards provided by individual state departments (such as Commerce, Energy, or Agriculture) to support businesses that contribute to the state's economic health. Unlike federal grants, which may have a national scope, state grants are specifically designed to promote regional innovation, job creation, and the development of local industries. These funds are non-dilutive, meaning the state does not take an equity stake in the company. (National Association of State Energy Officials, 2024)

<br>



    <br>2.	The best type of companies to raise money via state agencies are those that align with the specific strategic priorities of that state—such as manufacturing, green energy, agriculture, or tech-enabled services. These companies typically have a presence in the state (or a plan to relocate), a clear path toward job creation, and a project that requires capital to move from the research phase to market readiness. State agencies often prioritize companies that can leverage the grant to attract additional private investment. (SBA.gov, 2025)

<br>


    <br>3.	State Agency Grants emerged as a prominent tool in the late 20th century as states began competing to become "innovation hubs." Following the success of early state-led initiatives like the North Carolina Biotechnology Center (est. 1984), other states developed agencies focused on "Technology-Based Economic Development" (TBED). These programs were accelerated by the 2008 financial crisis and the 2021 ARPA funding, which provided states with additional capital to support small businesses and infrastructure projects. (State Science & Technology Institute, 2021)

<br>

    <br>4.	While state grants offer valuable funding, they come with specific administrative risks. Many state grants operate on a "reimbursement basis," meaning the company must spend the money first and then submit documentation for repayment, which can strain cash flow. Additionally, state programs are subject to the legislative budget process; a change in the governor's office or state house can lead to the sudden defunding of a specific grant program. Compliance often requires strict "clawback" provisions, where a company may have to return funds if job creation targets are not met. (Journal of State Taxation, 2024)

<br>

    <br>5.	To raise capital via a state agency, a company must demonstrate strong local impact and technical merit. The process usually involves a multi-stage application starting with a Letter of Intent (LOI), followed by a full proposal detailing the project’s economic benefits to the state. Applicants must provide evidence of financial stability and a clear plan for how the funds will result in measurable outcomes, such as new hires or patent filings. Establishing a relationship with the state’s economic development office prior to application is often a key factor in success. (Grants.gov Learning Center, n.d.)
    </p>

                            

    <p><u><b>References</u></b><br>

    <br>National Association of State Energy Officials (NASEO). (2024). State Energy Grant Programs and Policy. <a href=" https://naseo.org/state-energy-offices"> https://naseo.org/state-energy-offices</a>

<br>

     <br>SBA.gov. (2025). State Trade Expansion Program (STEP). <a href=" https://www.sba.gov/funding-programs/grants/state-trade-expansion-program-step"> https://www.sba.gov/funding-programs/grants/state-trade-expansion-program-step</a>

<br>

   <br>State Science & Technology Institute (SSTI). (2021). The History of State Investment in Innovation. <a href=" https://ssti.org/blog/history-tbed-investment"> https://ssti.org/blog/history-tbed-investment</a>

<br>

   <br>Journal of State Taxation. (2024). Risks and Compliance in State Incentive Programs.  <a href="https://www.wolterskluwer.com/en/solutions/cch-axcess/tax-journals">https://www.wolterskluwer.com/en/solutions/cch-axcess/tax-journals</a>

<br>

   <br>Grants.gov Learning Center. (n.d.). Grant Eligibility and State-level Funding.  <a href="https://www.grants.gov/web/grants/learn-grants/grant-eligibility.html">https://www.grants.gov/web/grants/learn-grants/grant-eligibility.html</a>

<br>


    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	In-State Registration – Must be legally incorporated or registered to do business in the specific state.
<br>•	Physical Presence – Often requires a headquarters, office, or manufacturing facility within state borders.
<br>•	Tax Compliance – Must have a "Certificate of Good Standing" from the State Department of Revenue.
<br>•	Employment Verification – Commitment to hiring a certain percentage of state residents.
<br>•	Industry Eligibility – Business must fall within a "priority sector" defined by the state agency.
<br>•	Clean Legal Record – No active litigation with the state or history of environmental/labor violations.
<br>•	Small Business Size Standards – May need to meet specific employee or revenue caps (e.g., under 500 employees).
<br>•	Matching Funds – Many state grants require the company to provide a 1:1 "match" in private capital.
<br>•	SAM.gov Registration – Required if the state grant is partially funded by federal "pass-through" money.




    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•State Tax ID & Registration – Formal documentation of the business's identity within the state.
<br>•	Certificate of Good Standing – Issued by the Secretary of State.
<br>•	Economic Impact Statement – Detailed projection of jobs created and local tax revenue generated.
<br>•	Project Work Plan – A timeline of milestones, deliverables, and specific tasks.
<br>•	Project Budget & Match Proof – Documentation showing where the matching funds are coming from (e.g., bank statements).
<br>•	Lease Agreement or Deed – Proof of physical location within the state.
<br>•	Resumes of Key Personnel – Highlighting the expertise of the team executing the project.
<br>•	W-9 Form – Required for the state to issue payments.
<br>•	Environmental Impact Report – (If applicable) ensuring the project meets state environmental standards.
<br>•	Quarterly Progress Reports – Templates for how the company will report back to the agency.
	



    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantsstateagenciesfaq(request):
    introduction = mark_safe("""<p><b><center>Capital Market: Grants<br>

    State Agencies</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1.	What are state agency grants, and how do they differ from other funding options? </u></b><br>

    •Answer: State agency grants are non-repayable funds provided by state or regional government agencies to support startups, small businesses, research initiatives, or community projects. Unlike loans or equity investments, they do not require repayment or ownership dilution. These grants focus on stimulating economic growth, innovation, workforce development, or social impact within the state.
</p>

                            

     <p><u><b>2.	What types of businesses are best suited for state agency grants? </u></b><br>

    •Answer: State agency grants typically target early-stage startups, small and medium-sized enterprises (SMEs), research institutions, and social enterprises that align with state economic, social, or technological priorities. Companies focused on innovation, job creation, sustainability, or community development are often the best fit.
</p>


                            

    <p><u><b>3.	How much funding can I expect from a state agency grant? </u></b><br>

    •Answer: Funding amounts vary widely depending on the program. Small grants may range from $5,000 to $50,000, while larger grants for research or innovation projects can exceed $500,000. Funding is usually earmarked for specific project needs, such as product development, workforce training, research, or equipment purchases.
</p>


                            

   <p><u><b>4.	How quickly can I access grant funds after being approved? </u></b><br>

    •Answer: Disbursement timelines vary by state program but are generally slower than private capital. Funds are often provided within a few weeks to several months after approval, and many programs release funding in stages tied to project milestones or reporting requirements.
</p>


                            

    <p><u><b>5.	What are the costs of participating in a state agency grant program? </u></b><br>

    •Answer: Application fees are usually low or free, but recipients must dedicate time and resources to comply with reporting, documentation, and performance measurement requirements. The “cost” is primarily administrative effort rather than financial repayment.
</p>


                            

   <p><u><b>6.	Do I have to give up equity to receive a state agency grant? </u></b><br>

    •Answer: No. State agency grants are non-dilutive, meaning you retain full ownership and control of your business.
</p>


                            

 <p><u><b>7.	Can a company still raise capital from other sources while receiving a state grant? </u></b><br>

    •Answer: Yes. Most state grants allow recipients to raise additional capital from private investors, venture capital, or other grants, as long as grant conditions are met and there are no conflicts with fund usage. Some grants may require notification or approval before combining funds.
</p>
                            

     <p><u><b>8.	What are the key benefits of state agency grants over traditional VC or loans? </u></b><br>

    •Answer: Key benefits include non-repayable funding with no interest or equity dilution, alignment with state economic or social development goals, credibility and visibility with government agencies, and access to mentorship, networking, and additional state-backed support programs.
</p>

                            

   <p><u><b>9.	What resources and support can I expect from state agency grants? </u></b><br>

    •Answer: State grants may provide access to mentorship, workshops, and technical assistance; connections to local industry partners, investors, or government programs; support for training, R&D, or compliance with regulatory standards; and in some cases, networking events, marketing support, or access to research facilities.
</p>

                            

    <p><u><b>10.	What happens after the grant period ends? </u></b><br>

    •Answer: After completing the project, recipients may need to submit final reports, financial statements, or impact assessments. Many state agencies also provide opportunities for follow-up funding, introductions to additional programs, or participation in state-sponsored events to further business growth.
</p>

                        

   <p><u><b>11.	Are there any risks associated with state agency grants? </u></b><br>

    •Answer: Risks include administrative burden for reporting and compliance, funding limitations as grants may not cover all project expenses, project delays or unmet milestones affecting future eligibility, and no guarantee of long-term business success.
</p>

                        

  <p><u><b>12.	How do state agency grants compare to other forms of government funding, such as municipal or federal grants? </u></b><br>

    •      Answer: State agency grants are larger and more structured than municipal grants but usually smaller and less complex than federal grants. Municipal grants focus on local priorities, while state grants can target broader regional initiatives. Federal grants may offer more funding but come with more stringent reporting and eligibility requirements.                  

</p>


   <p><u><b>13.	Can I apply for a state agency grant if I have already received other funding? </u></b><br>

    •Answer: Yes, many state grants allow recipients to combine funds from other sources, including private investment, federal grants, or loans, as long as fund usage complies with all grant terms and reporting requirements.
</p>

                        

 <p><u><b>14.	What types of projects typically get approved for state grants? </u></b><br>

    •Answer: Projects that demonstrate innovation or technological advancement, job creation or workforce development, economic growth or sustainability initiatives, social impact or community benefits, and alignment with state economic or strategic goals.
</p>

                        

  <p><u><b>15.	How can I increase my chances of receiving a state agency grant? </u></b><br>

    •Answer: Develop a clear, detailed project plan aligned with state priorities, demonstrate measurable impact (e.g., job creation, revenue growth, social benefit), show a strong team capable of executing the project, prepare a realistic budget and timeline, and follow application instructions carefully to meet all eligibility requirements.
</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantsstateagenciestwelve(request):
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

    Capital Type: State Agencies</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

State agency grants are suitable for idea-stage to early-growth businesses, including startups, SMEs, and projects with state-aligned objectives. Grants typically support innovation, workforce development, technology adoption, or regional economic growth.
    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Eligible entities usually include formally registered businesses, such as sole proprietorships, partnerships, LLCs, and corporations. Some grants may also target non-profits or collaborations with academic institutions. Preference is often given to local businesses or entities operating within the state/province.
    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Most state grants do not require prior funding, but some may require matching funds, co-financing, or owner contributions to demonstrate commitment. Businesses without prior capital are often prioritized to encourage growth and innovation.

    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Grants operate outside equity and debt markets. Previous funding, including venture capital or loans, generally does not disqualify an applicant, provided the grant’s purpose is met. These are non-dilutive, non-repayable funds.
    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
State grants typically provide small to moderate funding, often intended to cover project costs, research, pilot programs, or workforce initiatives rather than full business expansion. Amounts vary by program and state budget allocations.

    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Grant funding is not tied to traditional investment rounds. Funding occurs per program or project cycle, often aligned with state fiscal calendars.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Disbursement usually happens in phased tranches, for example:
<br>•	Initial advance after approval
<br>•	Subsequent payments after milestone verification
<br>•	Final disbursement upon project completion
This ensures accountability and proper use of public funds.


    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds must be used strictly for approved purposes, such as:
<br>•	Educational programs, training, or scholarships
<br>•	Workforce development initiatives
<br>•	Research and innovation projects
<br>•	Community or regional development programs
Funds cannot be used for personal expenses, debt repayment, or unrelated activities.

    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>
Financial risk is low, as grants are non-repayable. Compliance risk is high, requiring reporting, audits, and performance verification. Misuse can result in clawbacks or future disqualification.

    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The direct cost of capital is zero, since grants do not need repayment or equity dilution. Indirect costs include administrative effort, reporting, and compliance with grant conditions.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

Upfront costs are generally minimal, limited to proposal preparation, documentation, and compliance setup. There are no application fees in many state programs.
    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

The timeline can vary widely, usually 2–6 months, depending on application cycles, state approval processes, and budget availability.
</p>
"""

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)