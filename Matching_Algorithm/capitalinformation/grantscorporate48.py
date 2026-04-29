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

def grantscorporate(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Grants</b></u><br>
    Capital Type: Corporate Grants </center></p>
    <p><b><u>Introduction</u></b><br>
A Corporate Grant is ideal for early-stage and growth-stage companies that require non-dilutive capital to fund research, pilot programs, or innovation initiatives without giving up equity or taking on repayment obligations. It is designed so that capital is provided by a corporation to advance predefined strategic, technical, or impact-driven objectives rather than to generate direct financial returns. {n} fits that definition. In 2026, corporate grants have become a standardized tool within corporate innovation, ESG, and open-ecosystem strategies. Large multinational corporations increasingly deploy grant capital to accelerate external innovation in sectors such as climate technology, fintech infrastructure, artificial intelligence, healthcare, advanced manufacturing, and supply-chain resilience. These programs are often globally competitive and milestone-driven. While corporate grants eliminate dilution and balance-sheet risk, they introduce operational, compliance, and strategic alignment risks. Funds are typically restricted to approved use cases, subject to ongoing reporting obligations, and governed by enforceable contractual terms.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Corporate Grant is a non-dilutive funding instrument that provides capital from a for-profit corporation to an external entity—such as a startup, research institution, or innovation partner—without creating an equity ownership or debt repayment obligation. The funding is awarded to advance predefined strategic, technical, or impact-oriented objectives rather than to generate direct financial returns. (McKinsey & Company, 2025)
<br>


    <br>2.  Corporate grants sit outside the Capital Stack, meaning the grantor does not receive shares, voting rights, interest, or liquidation preference. However, the recipient remains contractually bound by the grant terms, and failure to comply may result in remedies such as funding suspension, termination, or repayment through clawback provisions. (Harvard Business Review, 2025)
<br>

    <br>3. Corporate grants are governed by a legally binding Grant Agreement that defines the scope of work, permitted use of funds, milestone-based disbursement schedules, reporting requirements, and intellectual property treatment. Unlike equity financing, these agreements prioritize performance compliance over financial upside. (Boston Consulting Group, 2026)
<br>
    <br>4.From a risk perspective, corporate grants shift financial risk away from the recipient while introducing execution, compliance, and strategic alignment risks. Because funds are restricted and monitored, recipients must ensure that grant-funded activities do not conflict with future investor expectations, acquirer diligence, or independent commercialization plans. (OECD, 2025)
<br>
    <br>5.
From an accounting and process standpoint, corporate grants are typically recorded as Other Income or Deferred Revenue, depending on whether performance obligations remain outstanding at the time of receipt. Funds are often disbursed in tranches tied to verified milestones, making corporate grants slower to deploy than equity but significantly less dilutive and balance-sheet intensive. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>McKinsey & Company. (2025). Corporate Innovation and External Grant Programs. <a href="https://www.mckinsey.com/capabilities/innovation">https://www.mckinsey.com/capabilities/innovation</a>
<br>
    <br>Harvard Business Review. (2025). How Corporations Fund External Innovation. <a href="https://hbr.org/2025/innovation-funding">https://hbr.org/2025/innovation-funding</a>
<br>
    <br>Boston Consulting Group (BCG). (2026). Open Innovation and Strategic Grant Models. <a href="https://www.bcg.com/publications/2026/open-innovation">https://www.bcg.com/publications/2026/open-innovation</a>
<br>
    <br>OECD. (2025). Public and Private Grant Mechanisms for Innovation. <a href="https://www.oecd.org/innovation">https://www.oecd.org/innovation</a>
<br>
    <br>Deloitte. (2025). Accounting Treatment of Grants and Incentives. <a href="https://www2.deloitte.com/grants-accounting">https://www2.deloitte.com/grants-accounting</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Eligibility Criteria - Industry focus, geography, company stage, and thematic alignment
<br>•   Use-of-Funds Restrictions - Capital limited to approved activities and budgets
<br>•   Milestone Definitions - Technical, commercial, or research deliverables
<br>•   Reporting Obligations - Periodic financial and progress disclosures
<br>•   Intellectual Property Clauses - Foreground and background IP ownership terms
<br>•   Publicity Rights - Rules governing announcements, logos, and branding
<br>•   Clawback Provisions - Conditions under which funds must be repaid
<br>•   Compliance & Sanctions Checks - KYC, AML, export control, and ethics compliance


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Grant Application / Proposal - Technical and strategic justification
<br>•   Grant Agreement - Primary legal contract governing the award
<br>•   Statement of Work (SOW) - Milestones, deliverables, and timelines
<br>•   Approved Budget & Cost Schedule - Permitted expenses and categories
<br>•   IP Schedule - Ownership, licensing, and usage rights
<br>•   Reporting Templates - Financial and performance reporting formats
<br>•   Compliance Certifications - Legal and regulatory confirmations
<br>•   Termination & Clawback Addendum - Remedies for non-performance

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def grantscorporatefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Grants<br>
    Corporate Grants</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a corporate grant?</u></b><br>
    •Answer: A corporate grant is non-dilutive funding provided by a corporation or its foundation to support projects or initiatives without receiving equity in return.
</p>

    <p><u><b>2. Who provides corporate grants?</u></b><br>
    •Answer: Corporate grants are typically provided by a company's CSR, ESG, sustainability, or corporate foundation teams.
</p>

    <p><u><b>3. Who is eligible to receive a corporate grant?</u></b><br>
    •Answer: Eligible recipients may include nonprofits, NGOs, research institutions, social enterprises, and in some cases for-profit startups.
</p>

    <p><u><b>4. When are corporate grants typically used?</u></b><br>
    •Answer: Corporate grants are used to fund social impact programs, research, pilot projects, and initiatives aligned with corporate priorities.
</p>

    <p><u><b>5. Are corporate grants dilutive?</u></b><br>
    •Answer: No, corporate grants are non-dilutive and do not require giving up equity or ownership.
</p>

    <p><u><b>6. How do organizations apply for a corporate grant?</u></b><br>
    •Answer: Organizations apply through a structured application process that includes submitting a proposal, budget, and supporting documents.
</p>

    <p><u><b>7. What documents are typically required for a corporate grant application?</u></b><br>
    •Answer: Common documents include organizational registration, project proposal, budget, timeline, impact metrics, and financial information.
</p>

    <p><u><b>8. How are corporate grant proposals evaluated?</u></b><br>
    •Answer: Proposals are evaluated based on alignment with corporate goals, feasibility, expected impact, and organizational capacity.
</p>

    <p><u><b>9. Is due diligence required for corporate grants?</u></b><br>
    •Answer: Yes, corporates usually conduct due diligence covering governance, financial controls, and compliance.
</p>

    <p><u><b>10. How are corporate grant funds disbursed?</u></b><br>
    •Answer: Funds are typically disbursed in tranches or milestones linked to approved deliverables or progress reports.
</p>

    <p><u><b>11. Are reporting requirements associated with corporate grants?</u></b><br>
    •Answer: Yes, recipients must submit periodic progress and financial reports as specified in the grant agreement.
</p>

    <p><u><b>12. How is impact measured in corporate grants?</u></b><br>
    •Answer: Impact is measured using predefined KPIs such as outcomes achieved, beneficiaries reached, and milestones completed.
</p>

    <p><u><b>13. Can corporate grants be renewed or extended?</u></b><br>
    •Answer: Yes, grants may be renewed or extended based on performance and continued alignment with corporate objectives.
</p>

    <p><u><b>14. What are the risks associated with corporate grants?</u></b><br>
    •Answer: Risks include strict compliance requirements, reporting burden, funding delays, or early termination.
</p>

    <p><u><b>15. When should an organization pursue a corporate grant?</u></b><br>
    •Answer: An organization should pursue a corporate grant when it has a well-defined impact project aligned with corporate priorities and the ability to meet compliance and reporting requirements.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def grantscorporatetwelve(request):
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
    Capital Type: Corporate Grants</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Corporate grants are best suited for early-stage to growth-stage companies, including startups that are developing innovative products, conducting pilots, or aligning with a corporation's strategic priorities. Some programs also support mature companies working on specific initiatives.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible entities typically include LLCs, C-Corps, S-Corps, nonprofits, and research institutions. Sole proprietorships may qualify in limited cases, but most corporate grant programs prefer formally registered organizations.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Companies may have little to no prior funding, though some corporate grants favor organizations that can demonstrate prior progress, pilot results, or co-funding. Equity funding is generally not required.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Corporate grants operate within the private non-dilutive funding market, sponsored by corporations seeking innovation, research collaboration, ESG impact, or supplier diversity initiatives.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Grant amounts typically range from $10,000 to $500,000, depending on program scope, corporate sponsor, and project complexity. Some programs may offer follow-on funding or contracts.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Corporate grants are not capital rounds and do not involve equity issuance or debt obligations. They are often used alongside equity or debt financing.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are commonly disbursed in milestone-based tranches, tied to project deliverables, reporting requirements, or performance benchmarks.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Permitted uses typically include:
<br>•   Research and development
<br>•   Pilot programs or proof-of-concept projects
<br>•   Technology development
<br>•   Workforce and operational costs related to the grant
Funds are restricted to approved project expenses and require detailed reporting.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is low to moderate, primarily related to compliance, reporting obligations, and performance milestones. Failure to meet requirements may result in delayed or reduced funding.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is low, as grants are non-dilutive and non-repayable. Indirect costs include administrative effort, reporting, and potential IP or publicity obligations.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are low to moderate, including proposal preparation, legal review, and compliance setup. No repayment or interest costs apply.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is moderate to slow, often 3-9 months, depending on application cycles, review processes, and milestone approvals.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
