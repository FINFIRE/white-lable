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

def grantsresearch(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Grants</b></u><br>
    Capital Type: Research Grants </center></p>
    <p><b><u>Introduction</u></b><br>
Research Grants, primarily focused on Small Business Innovation Research (SBIR) and Small Business Technology Transfer (STTR), are ideal for companies seeking non-dilutive capital to fund high-risk, high-reward technological innovation. They are designed so that federal agencies can meet specific R&D needs while helping small businesses commercialize "deep tech" that might be too early-stage for private investors. {n} fits that definition. These grants are often referred to as "America's Seed Fund." In Fiscal Year 2024, the program hit record highs, with 11 federal agencies (like NASA, NIH, and the DoD) allocating over $4 billion in total funding to small firms. Unlike venture capital, these grants require zero equity and zero repayment. A typical Phase I award ranges from $50,000 to $275,000 for feasibility studies, while Phase II awards for prototype development can reach $1 million to $2 million. While research grants offer a "free" lifeline for innovation, the competition is fierce (often a <15% success rate), and the administrative burden—including rigid accounting, technical reporting, and a 6-to-9-month application cycle—requires a significant commitment from the founding team.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.Research Grants (SBIR/STTR) are competitive awards that fund a small business's efforts to solve a specific technical problem identified by a federal agency. SBIR is focused on the small business alone, whereas STTR legally requires the business to partner with a non-profit research institution (like a university). These grants are unique because they focus on "technical merit" and "commercial potential" rather than just credit scores or collateral. (SBIR.gov, 2025)
<br>


    <br>2.  The best type of companies to raise capital via research grants are science-led startups (Biotech, Aerospace, Clean Energy, AI) that are still in the "technical valley of death"—meaning they have a proven concept but need significant R&D to build a working prototype. It is particularly effective for companies where the intellectual property (IP) is the primary asset. (National Science Foundation, 2025)
<br>

    <br>3. The SBIR program emerged from the Small Business Innovation Development Act of 1982. It was created to counter the trend of federal R&D dollars going almost exclusively to large defense contractors. By mandating that agencies with extramural R&D budgets over $100 million set aside a percentage (currently 3.2%) for small firms, it decentralized American innovation. The STTR program followed in 1992 to bridge the gap between academic research and commercial products. (Congressional Research Service, 2025)
<br>
    <br>4.While research grants provide equity-free cash, they carry "pivot and compliance" risks. Once a grant is awarded, the project scope is legally fixed; if the market changes and you need to pivot your technology, you may lose the funding. Additionally, agencies require Federal Acquisition Regulation (FAR)-compliant accounting. If an audit finds you spent "research" money on "marketing" or personal expenses, it can lead to heavy fines or debarment from federal contracting. (Skipso, 2025)
<br>
    <br>5.
To raise capital via research grants, a founder must register in multiple federal databases (SAM.gov, Grants.gov, eRA Commons). The core of the application is a "Technical Proposal," often 15-20 pages, detailing the scientific approach, the qualifications of the Principal Investigator (PI), and a commercialization plan. Success usually requires a dedicated grant writer or a founder with a strong academic background who can navigate the complex "Notice of Funding Opportunities" (NOFOs). (USDA NIFA, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>SBIR.gov. (2025). About the SBIR and STTR Programs. <a href="https://www.sbir.gov/about">https://www.sbir.gov/about</a>
<br>
    <br>National Science Foundation (NSF). (2025). America's Seed Fund: NSF SBIR/STTR Portfolio. <a href="https://seedfund.nsf.gov/">https://seedfund.nsf.gov/</a>
<br>
    <br>Congressional Research Service (CRS). (2025). Small Business Research Programs: Issues for Reauthorization. <a href="https://www.congress.gov/crs-product/IF12874">https://www.congress.gov/crs-product/IF12874</a>
<br>
    <br>Skipso. (2025). What is Grant Funding? Understanding Its Importance and Impact. <a href="https://www.skipso.com/resources/what-is-grant-funding-en">https://www.skipso.com/resources/what-is-grant-funding-en</a>
<br>
    <br>USDA NIFA. (2025). Small Business Innovation Research (SBIR) Programs. <a href="https://www.nifa.usda.gov/grants/programs/sbir-sttr">https://www.nifa.usda.gov/grants/programs/sbir-sttr</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   U.S. Ownership - Must be at least 51% owned and controlled by U.S. citizens or permanent resident aliens
<br>•   Size Standard - Must be a "small business" with 500 or fewer employees (including affiliates)
<br>•   Principal Investigator (PI) - The PI's primary employment (over 50%) must be with the small business at the time of award
<br>•   Location of Work - All research and development work must be performed within the United States
<br>•   Performance Percentages - For SBIR Phase I, the small business must perform at least 67% of the work; for Phase II, at least 50%
<br>•   IP Ownership - The small business must generally own or have a legal path to the intellectual property developed
<br>•   Accounting Compliance - Must be able to track grant funds separately from general business revenue in an audited ledger


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   SAM.gov Registration - Required Active Status (UEI number)
<br>•   Technical Proposal - The core of the application (usually 15 pages)
<br>•   Biographical Sketches - Resumes for the PI and key senior personnel in specific federal formats
<br>•   Facilities & Other Resources - Description of the lab or office space where research will occur
<br>•   Budget Justification - Detailed breakdown of how every dollar will be spent (salaries, equipment, travel)
<br>•   Current and Pending Support - Disclosure of all other funding sources to avoid "double-dipping"
<br>•   Commercialization Plan - (Required for Phase II) A roadmap of how the product will reach the market
<br>•   Letters of Support - From potential customers or investors to prove market interest

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def grantsresearchfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Grants<br>
    Research Grants</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are Research Grants, and how do they differ from other funding options?</u></b><br>
    •Answer: Research Grants are non-repayable funds provided by government agencies, institutions, or private organizations to support specific research projects, allowing recipients to pursue innovation without giving up equity or incurring debt.
</p>

    <p><u><b>2. What types of businesses or organizations are best suited for Research Grants?</u></b><br>
    •Answer: Universities, research institutions, startups, and companies with innovative or scientific projects, particularly in technology, healthcare, environmental science, or social impact, are ideal candidates.
</p>

    <p><u><b>3. How much funding can I expect from a Research Grant?</u></b><br>
    •Answer: Funding varies widely depending on the grant provider, project scope, and duration, ranging from $5,000 to several million dollars.
</p>

    <p><u><b>4. How quickly can I access Research Grant funds?</u></b><br>
    •Answer: Access depends on the grant approval process, typically taking a few weeks to several months after submission, review, and award notification.
</p>

    <p><u><b>5. What are the costs of applying for a Research Grant?</u></b><br>
    •Answer: Costs may include time spent on proposal writing, administrative fees, and compliance reporting, but there is usually no repayment requirement.
</p>

    <p><u><b>6. Do I have to give up equity or ownership for a Research Grant?</u></b><br>
    •Answer: No, Research Grants are non-dilutive, meaning recipients retain full ownership of their business or research outcomes.
</p>

    <p><u><b>7. Can I still raise capital from other sources while receiving a Research Grant?</u></b><br>
    •Answer: Yes, grants can be combined with other funding sources such as private investment, loans, or internal funds, though some grants may have restrictions on overlapping funding.
</p>

    <p><u><b>8. What are the key benefits of receiving a Research Grant over traditional investment or loans?</u></b><br>
    •Answer: Benefits include non-dilutive funding, credibility and validation of the project, access to networks, and flexibility to focus on research rather than immediate revenue generation.
</p>

    <p><u><b>9. What resources and support can I expect from a Research Grant?</u></b><br>
    •Answer: Support may include mentorship, access to lab facilities, networking opportunities, technical guidance, and administrative assistance from the grant provider.
</p>

    <p><u><b>10. What happens after the Research Grant project ends?</u></b><br>
    •Answer: Recipients are often required to submit final reports, present findings, and share results with the funding organization, which may also provide opportunities for follow-on funding or collaboration.
</p>

    <p><u><b>11. Are there any risks associated with Research Grants?</u></b><br>
    •Answer: Risks include failure to meet project milestones, non-compliance with grant requirements, misuse of funds, and reliance on grant funding without sustainable revenue sources.
</p>

    <p><u><b>12. How do Research Grants compare to other grants or private funding?</u></b><br>
    •Answer: Research Grants are highly targeted, non-repayable, and non-dilutive, unlike loans which must be repaid or private equity which requires ownership exchange.
</p>

    <p><u><b>13. Can I apply for a Research Grant if I have already received other grants?</u></b><br>
    •Answer: Yes, many grant providers allow multiple grants, but applicants must disclose existing funding and ensure no overlap in project scope or budget restrictions.
</p>

    <p><u><b>14. What types of projects typically get approved for Research Grants?</u></b><br>
    •Answer: Projects with innovative, evidence-based, and measurable outcomes in science, technology, social impact, or healthcare are most likely to be approved.
</p>

    <p><u><b>15. How can I increase my chances of receiving a Research Grant?</u></b><br>
    •Answer: Prepare a well-structured proposal, demonstrate project feasibility, show alignment with grant objectives, provide a clear budget, and highlight team expertise.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def grantsresearchtwelve(request):
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
    Capital Type: Research Grants</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Research grants are ideal for idea-stage to early-growth organizations, particularly startups, academic institutions, or SMEs conducting R&D, innovation, or scientific research. They help cover costs for projects that may not yet be commercially viable.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities include registered businesses, academic institutions, non-profits, and research organizations. Some programs require partnerships between academia and industry.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Most research grants do not require prior funding, but demonstrating preliminary research, prior results, or a clear plan strengthens eligibility. Some grants may require matching funds.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Grants are non-market-based. Prior funding from equity, debt, or venture capital does not typically disqualify an applicant, though the grantor may assess funding efficiency and duplication of resources.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Grant amounts vary widely, from small seed grants to multi-million-dollar awards, depending on the scope of the research and the funding body. They are intended to cover research costs rather than general business expansion.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Research grants are not tied to traditional capital rounds. Funding is allocated per project cycle or proposal approval.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are often disbursed in phased tranches, ensuring accountability and proper use of funds: initial funding upon approval, subsequent milestone-based payments, and final payment after completion and reporting.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Funds must be used strictly for research-related activities, such as:
<br>•   Laboratory equipment and materials
<br>•   Personnel and researcher salaries
<br>•   Data collection and analysis
<br>•   Travel and dissemination of results
Funds cannot be used for unrelated business expenses or personal use.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Financial risk is low, as grants are non-repayable. Compliance risk is moderate to high, with reporting, audits, and performance monitoring required. Failure to meet grant conditions can result in clawbacks.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is zero, as research grants do not require repayment or equity dilution. The indirect cost is administrative effort and compliance burden.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are generally low to moderate, mainly covering proposal preparation, documentation, and compliance setup.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
The timeline for receiving research grants varies, typically 3-12 months, depending on program complexity, review cycles, and funding body decisions.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
