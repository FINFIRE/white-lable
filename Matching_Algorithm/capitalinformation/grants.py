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


def grants(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Grants</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Grants are an ideal source of non-dilutive capital for early to growth-stage companies seeking funding for innovation, research, development, or expansion without giving up equity. They are designed to support ventures that demonstrate strong potential for social, technological, or economic impact. {n} fits that definition. Grants have been a reliable and growing source of capital for startups and small businesses for decades. For example, in FY2023, the U.S. federal government awarded over $970 billion in grant funding, with a significant portion going to small businesses and startups through programs like SBIR, STTR, and USDA innovation grants. Additionally, corporate and private foundation grants contributed an estimated $90 billion in funding to businesses and nonprofit ventures in 2023. In the technology and clean energy sectors alone, more than $20 billion in grants were allocated by state and federal programs to fuel innovation and job creation. On average, individual grant awards ranged from $25,000 to $500,000, depending on the initiative and funding body. There are 6 types of grants that we can match you with: 1) Corporate Grands, 2) Education Grants, 3) Government Grants, 4) Municipalities Grants, 5) Research Grants, 6) State Agencies Grants. We will match you with the best grant types based on your business needs.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Using grants to raise capital refers to the process by which companies, particularly startups and small to mid-sized businesses, obtain non-dilutive funding from government agencies, corporations, or private foundations to support specific business activities—such as research and development, product innovation, market expansion, or social impact initiatives. Unlike equity or debt financing, grants do not require repayment and do not involve giving up ownership or control of the business. Companies typically apply for grants by demonstrating their potential impact, innovation, or alignment with the grantor’s goals, and must often meet certain eligibility and reporting requirements to receive and maintain funding. (McColl, 2023)
<br>
    <br>2. There are several types of grants that companies can use to raise capital, each serving different purposes and stages of business development. Government grants—federal, state, or local—are the most common and often support innovation, research and development (R&D), clean energy, or job creation. Small Business Innovation Research (SBIR) and Small Business Technology Transfer (STTR) programs, for example, are key federal initiatives providing early-stage R&D funding. Corporate grants are offered by large companies to support startups and small businesses aligned with their strategic goals, such as sustainability, diversity, or supply chain development. Foundation or nonprofit grants often target social enterprises or mission-driven companies tackling issues like education, health, or environmental justice. Regional or economic development grants are available to companies locating or expanding in certain geographic areas to boost local economies. Each grant type typically has its own eligibility criteria, funding limits, and reporting requirements. (Daugherty, 2024)
<br>
    <br>3. The history of grants as a means of funding dates back centuries, but their use in modern business and innovation funding gained momentum in the 20th century. Government-backed grants became prominent during and after the New Deal era in the 1930s, when the U.S. government began using financial incentives to stimulate economic development and public welfare. In the post–World War II period, federal grant programs expanded significantly—especially for research and development—with the launch of agencies like the National Science Foundation (1950) and the Small Business Administration (1953). By the 1980s and 1990s, private foundations and corporations increasingly began offering grants to encourage innovation, entrepreneurship, and social impact initiatives. Programs such as SBIR (Small Business Innovation Research), started in 1982, formalized structured, competitive federal grant funding for small businesses developing cutting-edge technologies. Today, grants remain a critical tool used by governments, foundations, and corporations to spur economic growth, innovation, and community development without requiring repayment or equity ownership. (Federal Grants to State and Local Governments: A Brief History. n.d.)
<br>
    <br>4. The risks of grants for a company primarily stem from the complexity and competitive nature of the funding process. One significant risk is the time and resources required to apply, as grant applications often involve detailed proposals, financial reports, and compliance documentation. If a company does not receive the grant, this effort may result in wasted time and money. Additionally, grants are usually designated for specific uses, which can limit a company’s flexibility in how it deploys the funds. There’s also the risk of non-compliance with grant conditions, which can result in penalties, having to return funds, or damaging the company’s reputation. Finally, securing grants may not provide immediate capital, as the approval process can be lengthy, potentially leaving companies waiting for funds while they face urgent financial needs. (Nwokike, 2024)
<br>
    <br>5. To raise capital through grants, a company typically needs to meet specific eligibility criteria, which can vary depending on the grant type and the funding source. First, the company must be a legally registered entity, such as a corporation, LLC, or nonprofit, to ensure compliance with grant requirements. It should have a clear, well-developed business plan or project proposal that outlines how the grant funds will be used to achieve specific goals, such as product development, research, or social impact initiatives. Financial documentation, including recent financial statements and budgets, is often required to demonstrate the company’s financial health and its ability to manage the grant effectively. Additionally, companies need to demonstrate that their goals align with the objectives of the grantor, whether it’s a government agency, foundation, or corporation. A strong track record of prior work, such as successful past projects or similar grants, can also increase the likelihood of securing funding. Finally, a company must be prepared to comply with reporting requirements and the use of funds as specified by the grantor. (Applicant eligibility | Grants.gov. n.d.)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>McColl, B. (2023, July 14). US providing $20 billion in grants to help cut greenhouse gas emissions. Investopedia. <a href="https://www.investopedia.com/us-providing-usd20-billion-in-grants-to-help-cut-greenhouse-gas-emissions-7561434?">https://www.investopedia.com/us-providing-usd20-billion-in-grants-to-help-cut-greenhouse-gas-emissions-7561434?</a>
<br>
    <br>Daugherty, G. (2024, October 14). Small business owners need to know these tips to get a business grant. Investopedia. <a href="https://www.investopedia.com/small-business-grant-tips-8720448?">https://www.investopedia.com/small-business-grant-tips-8720448?</a>
<br>
    <br>Federal Grants to State and Local Governments: A Brief History. (n.d.). <a href="https://congressionalresearch.com/RL30705/document.php?">https://congressionalresearch.com/RL30705/document.php?</a>
<br>
    <br>Nwokike, F. (2024, October 11). The pros and cons of business grants. The Total Entrepreneurs. <a href="https://thetotalentrepreneurs.com/pros-and-cons-of-business-grants/?">https://thetotalentrepreneurs.com/pros-and-cons-of-business-grants/?</a>
<br>
    <br>Applicant eligibility | Grants.gov. (n.d.). <a href="https://www.grants.gov/applicants/applicant-eligibility?">https://www.grants.gov/applicants/applicant-eligibility?</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Legal Entity: The company must be a legally registered entity (LLC, corporation, nonprofit).
    <br>• Compliance: Must comply with local, state, and federal regulations.
    <br>• Registration: For government grants, the company must register with platforms like Grants.gov or SAM.gov.
    <br>• Eligibility Criteria: Some grants have specific eligibility based on business type (minority-owned, women-owned, etc.).
    <br>• Size & Revenue: Some grants are for small businesses with revenue or employee limits.
    <br>• Location: Certain grants may be region-specific.
    <br>• Sector Focus: Some grants are limited to specific industries or sectors.
    <br>• No Violations: The company must have no prior grant violations.
    <br>• Financial Health: Companies need to demonstrate good financial standing.
    <br>• Tax Registration: For certain grants, the company must be registered with tax authorities.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan/Proposal: A detailed plan outlining the company’s objectives, projects, and goals.
    <br>• Financial Statements: Recent balance sheets, income statements, and cash flow statements.
    <br>• Budget Plan: A clear breakdown of how grant funds will be used.
    <br>• Tax Returns: Most recent tax returns to demonstrate financial health and compliance.
    <br>• Registration Documents: Proof of business registration (LLC, corporation, nonprofit, etc.).
    <br>• Proof of Eligibility: Documentation supporting eligibility (minority-owned, veteran-owned, etc.).
    <br>• Project or Program Overview: Description of the specific project or initiative the grant will fund.
    <br>• Compliance Documents: Documents showing compliance with local, state, and federal regulations.
    <br>• Letters of Support: Testimonials or endorsements from partners, customers, or community members (if required).
    <br>• Matching Funds Documentation: If the grant requires matching funds, evidence of available funds.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantsfaq(request):
    introduction = mark_safe("""                    
    <p><b><u>FAQs</u></b></p>
                             
    <p><b><u>1.	What types of grants are available for companies?</u></b><br>
    • Answer: There are government grants, private foundation grants, corporate grants, and research grants. Each type typically has different eligibility requirements and focuses on various industries, sectors, or initiatives.
    </p>
                             
    <p><b><u>2.	How do I apply for a grant?</u></b><br>
    • Answer: To apply for a grant, you generally need to find suitable opportunities on platforms like Grants.gov (for federal grants) or private foundation websites. You must submit an application that includes a detailed proposal, financial documents, and other supporting materials.
    </p>
                             
    <p><b><u>3.	Who can apply for grants?</u></b><br>
    • Answer: Eligible applicants usually include for-profit companies, nonprofits, and startups, though specific grants may have restrictions, such as being available only to minority-owned, women-owned, or veteran-owned businesses.
    </p>
                             
    <p><b><u>4.	Do I need to repay grant money?</u></b><br>
    • Answer: Grants are typically non-repayable, which means you do not have to repay the funds if you meet the grant’s terms and conditions. However, if you misuse the funds or fail to meet the reporting requirements, you may have to return the money.
    </p>
                             
    <p><b><u>5.	What are the eligibility criteria for grants?</u></b><br>
    • Answer: Eligibility criteria vary depending on the grant, but common requirements include having a legal business entity (LLC, corporation, nonprofit), being in a specific industry or sector, and demonstrating a clear project or business need for the funds.
    </p>
                             
    <p><b><u>6.	How long does it take to receive grant funding?</u></b><br>
    • Answer: The timeline for receiving grant funding can range from a few weeks to several months, depending on the grant’s review and approval process. Some grants have specific cycles, so it’s important to apply well in advance.</p>
                             
    <p><b><u>7.	What is the grant application process?</u></b><br>
    • Answer: The application process typically involves researching available grants, preparing the required documents (business plan, financials, budget, etc.), submitting the application, and possibly going through an interview or review process before funding is approved.
    </p>
                             
    <p><b><u>8.	Are there any costs associated with applying for a grant?</u></b><br>
    • Answer: While applying for grants is generally free, there may be costs for professional services, such as hiring grant writers or legal assistance, which can help in preparing a strong application.</p>
                             
    <p><b><u>9.	What happens if I don’t win the grant?</u></b><br>
    • Answer: -	If your application is not selected, you may be able to apply for other grants in the future. Some grantors offer feedback on why your application wasn’t successful, which can help improve future submissions.</p>
                             
    <p><b><u>10. Can grants be used for any purpose?</u></b><br>
    • Answer: Grants are typically restricted to specific uses, such as product development, research, community initiatives, or social impact projects. Make sure your intended use aligns with the grant’s objectives.</p>
    
    <p><b><u>11. What happens if I don’t meet the grant’s reporting requirements?</u></b><br>
    • Answer: -	Failing to meet the reporting requirements can result in penalties, including the need to return the funds or being ineligible for future grants. It’s crucial to stay compliant with all conditions attached to the grant.</p>

    <p><b><u>12. Can grants be combined with other funding sources?</u></b><br>
    <br>• Answer: Yes, many grants can be used in conjunction with other funding sources like loans, private investments, or venture capital. However, some grants may require matching funds or have rules about using them with other financial support.
    </p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def grantstwelve(request):
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
        'Minimum $0 - Maximum $499' :'your cost estimate of $0 to $499 does not align with the cost required to fund you through a grant as it might not be sufficent to cover even the entries fees and paperworks.',
        'Minimum $500 - Maximum $999' :  'your cost estimate of $500 to $999 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',
        'Minimum $1000 - Maximum $2499' :  'your cost estimate of $1000 to $2,499 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',
        'Minimum $2500 - Maximum $4999' :  'your cost estimate of $2,500 to $4,999 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',
        'Minimum $5000 - Maximum $9999' :  'your cost estimate of $5000 to $9,999 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',
        'Minimum $10000 - Maximum $24999' : 'your cost estimate of $10,000 to $24,999 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',
        'Minimum $25000 - Maximum $49999' : 'your cost estimate of $25,000 to $49,999 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',
        'More than $50000+' : 'your cost estimate of more than $50,000 aligns with the cost required for raising fund through grants and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : '1 day to 1 week would not be sufficient to raise the capital within this period.',
        '1 Week to 2 Week' : '1 week to 2 weeks would not be sufficient to raise the capital within this period.',
        '2 Weeks to 4 Weeks' : '2 weeks to 4 weeks would not be sufficient to raise the capital within this period.',
        '1 Month to 2 Months' : '1 month to 2 months would be sufficient to raise the capital within this period given the documents are well prepared.',
        '2 Months to 3 Months' : '2 months to 3 months would be sufficient to raise the capital within this period given the documents are well prepared.',
        '3 Months to 6 Months' : '3 months to 6 months would be sufficient to raise the capital within this period.',
        '6 Months to 12 Months' : '6 months to 12 months would be sufficient to raise the capital within this period.',
        'More than 1 year' : 'More than 1 year would be sufficient to raise the capital within this period.',             
    }
    timeanalysis = up_front_time_options[upfronttime]


#ENTITY ANALYSIS IS NOT REQUIRED FOR THIS CAPITAL TYPE AND FOR EVERY OPTION SAME RESPONSE IS USED.
#    entity_options ={
#         "None (To be Determined)" : "does not qualify for incubator capital market.",
#         "Sole Proprietorship" : "and a portion should be allocated toward identifying and applying for aligned grants—especially those with matched funding requirements.",
#         "LLC" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity)." ,
#         "LP" : "does not qualify for incubator capital market.",
#         "GP" : "does not qualify for incubator capital market.",
#         "S Corporation" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity).",
#         "C Corp" : "qualifies, assuming it is officially registered, has clear founder agreements, and maintains basic financial hygiene (banking, bookkeeping, cap table clarity).",
#         "Other" : "does not qualify for incubator capital market.",
#    }
#    entityanalysis = entity_options[entity]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()     
    
    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Grants</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    Grant funding is especially well-suited for companies at {stage} stage, with mission-aligned initiatives addressing social, environmental, or technological challenges. {n}, if in the ideation, prototype, or MVP development stage, can leverage grants to de-risk innovation and achieve critical milestones without giving up equity. Ideal candidates often operate in sectors like cleantech, health, education, deep tech, or social impact.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Most grant programs support U.S.-based for-profit entities (LLCs, C Corporations) or nonprofits, depending on the funding source. For {n} to qualify, it must maintain good legal standing, clear ownership records, and—when applicable—meet eligibility criteria specific to the grant (e.g., small business classification under SBA rules, DEI certification, or sector focus). Many governments and private grants require companies to register with SAM.gov, Grants.gov, or state/local equivalents.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    If {n} has already raised {preraise} through friends and family, bootstrapping, accelerators, or other source; this signals a degree of traction that strengthens most grant applications. Many grant issuers prefer to fund companies that have demonstrated initial momentum or co-investment—helping validate feasibility while ensuring responsible use of non-dilutive funding.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    If pre-capital came via {premarketstr}, grants could offer a valuable complement to existing capital without further dilution. Grant-funded programs can also support parallel development, such as conducting user testing, building MVPs, or pursuing regulatory approvals. Strategic layering of grants with early capital helps {n} extend runway and reduce the burden of future equity fundraising.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    If {n} seeks to raise {raisegoal} over the next 12–18 months, securing $25K–$500K in grants can significantly offset product development, research, or operational expenses—thereby reducing the total capital required from investors. In some cases, grant alignment may make the company more attractive to mission-aligned VCs or impact funds.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Grants are non-dilutive and do not align with traditional equity capital rounds. However, they are particularly useful at the Pre-Seed, Seed, and even Series A stages when used to fund R&D, tech validation, or pilot programs. For {n}, integrating grants into a broader capital strategy can create compelling leverage points when raising future institutional rounds.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Grants are often disbursed in milestone-based tranches, requiring progress reports, deliverables, or spending documentation. Some smaller grants are disbursed in full upfront, while larger programs (especially federal or state-backed) may follow strict reimbursement models. {n} should prepare for tracking expenses, compliance reviews, and possibly hiring grant management support.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Grants can be used for a variety of early-stage activities, depending on the specific program:
    <br>• Research and development
    <br>• Prototype or MVP development
    <br>• Market feasibility or customer discovery
    <br>• Workforce development and hiring
    <br>• Export or international expansion
    <br>• Regulatory or certification processes

    <br><br>{n} must tailor its use-of-funds plan to align with the grant’s priorities and measurable outcomes.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Grant funding carries low financial risk but may introduce operational risk if reporting requirements are not met. Additionally, applying for grants can be time-intensive, with no guarantee of funding. For {n}, risk mitigation involves:
    <br>• Targeting highly aligned programs
    <br>• Allocating time or staff to the application process
    <br>• Maintaining compliance and documentation
    <br>• Engaging third-party grant writers or advisors when appropriate
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Grants are non-dilutive, making them the lowest-cost capital source available. However, indirect costs may include:
    <br>• Application time and effort
    <br>• Compliance and reporting overhead
    <br>• Restrictions on use of funds
    <br>• Delayed disbursement or reimbursement schedules

    <br><br>For {n}, these trade-offs are often worthwhile—especially if the grant supports a key milestone or proof-of-concept that increases valuation.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Grants generally require little to no upfront cost, but there may be indirect or optional expenses such as:
    <br>• Hiring a grant writer ($2K–$10K per application)
    <br>• Incorporating as a C Corp if required by the grantor
    <br>• Legal or accounting support for budgeting or compliance
    <br>• Average total cost might fall between $250 $10,000

    <br><br>If {n} has a {upfrontcost} allocated to R&D, product development, or fundraising, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    The timeline from application to grant disbursement typically spans 4–16 weeks, depending on the grant type (local, federal, corporate, etc.). Some programs have rolling deadlines, while others operate in fixed annual cycles. XYZ Company should create a grants calendar, with materials prepared in advance for:
    <br>• Business overview and mission alignment
    <br>• Detailed project proposal and budget
    <br>• Milestones, KPIs, and deliverables
    <br>• Past impact or testimonials, if applicable
    <br><br>Strong alignment with the grantor’s mission, clear outcomes, and a replicable or scalable plan will increase funding success. {n}'s required time of {timeanalysis}
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,timeanalysis=timeanalysis,costanalysis=costanalysis,premarketstr=premarketStr))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)