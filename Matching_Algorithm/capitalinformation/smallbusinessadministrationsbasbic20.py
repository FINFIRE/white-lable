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

def smallbusinessadministrationsbasbic(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBIC </center></p>
    <p><b><u>Introduction</u></b><br>
    Small Business Investment Companies (SBICs) are ideal for companies seeking growth-stage capital, including mezzanine financing, long-term loans, and equity investments. They are designed so that government-backed, privately owned and managed investment funds can help privately held small businesses scale, create jobs, and enhance American competitiveness. {n} fits that definition. The SBIC program has been a cornerstone of the U.S. financial landscape since 1958. By providing a government guarantee on the debt issued by these funds, the SBA allows SBIC managers to access low-cost capital to reinvest in American entrepreneurs. For example, in Fiscal Year 2023, the SBIC program provided over $8 billion in financing to more than 1,200 small businesses. Historically, the program has supported household names during their early growth phases, including Apple, FedEx, and Intel. On average, SBIC-backed companies gain access to between $2 million and $10 million in capital, though some funds specialize in smaller "Micro-SBIC" investments or much larger growth rounds. While SBIC funding offers a unique blend of private sector agility and government support, the strict "Small Business" size standards, regulatory reporting, and focus on domestic operations can limit eligibility for international or large-scale enterprises.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. SBICs are privately owned and managed investment funds that are licensed and regulated by the Small Business Administration (SBA). They use their own capital plus funds borrowed with an SBA guarantee to make equity and debt investments in qualifying small businesses. This unique "public-private partnership" model increases the volume of venture capital and private equity available to small businesses across the United States. (SBA.gov, 2024)<br><br>
    2. The best type of companies to raise money via SBICs are established small businesses with proven revenue, positive cash flow, or high-growth potential that need capital for expansion, equipment, or acquisitions. These companies must meet the SBA's size requirements—generally having a tangible net worth of less than $18 million and an average net income of less than $6 million for the previous two years. SBICs are particularly well-suited for businesses in manufacturing, technology, and underserved geographic markets. (U.S. House Committee on Small Business, 2023)<br><br>
    3. The SBIC program emerged as part of the Small Business Investment Act of 1958, created by Congress to bridge the gap between the availability of institutional capital and the needs of small, innovative firms. The program has evolved through several iterations, including the introduction of the "Debenture SBIC" for cash-flow-heavy businesses and the "Accrual SBIC" in 2023, designed to support longer-term equity investments in technology and infrastructure. (Congressional Research Service, 2024)<br><br>
    4. While SBICs offer flexible capital, there are specific regulatory risks. Because SBICs are government-regulated, the due diligence process can be more exhaustive than traditional VC rounds. Companies must maintain their "Small Business" status at the time of investment and agree to detailed reporting regarding their workforce and financial health. Additionally, because many SBICs use debt (leverage) from the SBA, they may have structured repayment requirements that could pressure a startup's monthly cash flow compared to pure equity. (National Association of Small Business Investment Companies, 2024)<br><br>
    5. To raise capital via an SBIC, a company does not apply directly to the SBA; instead, it must pitch to individual licensed SBIC fund managers. The process mirrors a traditional private equity or venture capital raise: founders must present a robust business plan, historical financial statements, and a clear exit strategy or repayment plan. Success requires demonstrating that the company meets SBA size standards and that the investment will be used for eligible "operating" purposes rather than passive real estate or speculation. (SBA Office of Investment and Innovation, n.d.)
    </p>
    <p><u><b>References</u></b><br>
    SBA.gov. (2024). SBIC Program Overview and Impact. https://www.sba.gov/funding-programs/investment-capital<br>
    U.S. House Committee on Small Business. (2023). The Role of SBICs in Small Business Growth. https://smallbusiness.house.gov/<br>
    Congressional Research Service (CRS). (2024). SBA Small Business Investment Company Program. https://crsreports.congress.gov/product/pdf/R/R41456<br>
    National Association of Small Business Investment Companies (NASBIC/SBAI). (2024). Industry Standards and Regulatory Compliance. https://www.sbia.org/<br>
    SBA Office of Investment and Innovation. (n.d.). Directory of SBIC Funds. https://www.sba.gov/document/support-sbic-directory
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • SBA Size Standards – Must qualify as a "small business" (Net worth &lt;$18M, Net income &lt;$6M, or industry-specific employee caps).<br>
    • U.S. Based Operations – At least 50% of employees and assets must be located within the United States.<br>
    • Eligible Industry – Cannot be a passive business, real estate developer, or engaged in gambling/speculation.<br>
    • Clean Character Record – Founders and key officers must pass background checks and "Statement of Personal History" (SBA Form 912).<br>
    • Conflict of Interest Review – Neither the SBA nor the SBIC associates can have a prohibited "self-dealing" interest in the company.<br>
    • Use of Proceeds Compliance – Funds must be used for business growth, not to pay off personal debt or buy out existing shareholders in a way that doesn't benefit the company.<br>
    • Certified Financials – Must provide at least two years of tax returns or audited/reviewed financial statements.
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • SBA Form 1031 – Portfolio Company Financing Report (to be completed during the deal).<br>
    • Detailed Business Plan – Including a 3-5 year financial projection and market analysis.<br>
    • Cap Table – Showing all current owners and any previous rounds of debt or equity.<br>
    • Historical Financials – Balance sheets and income statements for the last three fiscal years.<br>
    • Interim Financials – Year-to-date (YTD) financial reports.<br>
    • Organizational Documents – Articles of Incorporation, Bylaws, or Operating Agreement.<br>
    • Management Team Bios – Detailed professional backgrounds of all key executives.<br>
    • Customer/Contract List – Evidence of recurring revenue or major pending contracts.<br>
    • Debt Schedule – A list of all current liabilities and outstanding loans.
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasbicfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Small Business Administration (SBA)<br>
    SBIC</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is an SBA SBIC, and how does it differ from other funding options?</u></b><br>
    • Answer: An SBA Small Business Investment Company (SBIC) is a privately-owned investment fund licensed and regulated by the U.S. Small Business Administration that provides long-term debt and equity capital to small businesses, leveraging both private and government-backed funding.
    </p>
    <p><u><b>2. What types of businesses are best suited for SBIC funding?</u></b><br>
    • Answer: SBICs typically target small businesses with strong growth potential, innovative products or services, and scalable business models. Companies in technology, manufacturing, healthcare, and other high-growth industries often align well.
    </p>
    <p><u><b>3. How much funding can I expect from an SBIC?</u></b><br>
    • Answer: Funding amounts vary by SBIC, but they can provide equity investments or long-term loans ranging from $250,000 to several million dollars, often combined with private investment.
    </p>
    <p><u><b>4. How quickly can I access capital after approval?</u></b><br>
    • Answer: Access to funding depends on the SBIC's internal process, but generally, approved businesses receive funding within a few weeks to a few months, based on due diligence and investment terms.
    </p>
    <p><u><b>5. What are the costs of participating in an SBIC program?</u></b><br>
    • Answer: Costs may include interest on loans, equity dilution if the SBIC takes an ownership stake, and legal or administrative fees associated with the funding process.
    </p>
    <p><u><b>6. Do I have to give up equity to receive SBIC funding?</u></b><br>
    • Answer: Not always; SBICs can provide debt financing without equity, but many SBICs structure funding as equity or mezzanine investments, which may require giving up a portion of ownership.
    </p>
    <p><u><b>7. Can a company still raise capital from other sources while working with an SBIC?</u></b><br>
    • Answer: Yes, businesses can raise additional private or public capital, though SBIC agreements may include clauses regarding co-investment, preferred equity, or approval for other financings.
    </p>
    <p><u><b>8. What are the key benefits of SBIC funding over traditional VC or loans?</u></b><br>
    • Answer: SBICs provide access to substantial growth capital, government-backed leverage, flexible financing options (debt, equity, or mezzanine), and long-term support, often with lower cost of capital than traditional private investors.
    </p>
    <p><u><b>9. What resources and support can I expect from an SBIC?</u></b><br>
    • Answer: Beyond funding, SBICs often provide strategic guidance, operational support, industry connections, mentorship, and introductions to potential investors or partners.
    </p>
    <p><u><b>10. What happens after the SBIC investment or loan period ends?</u></b><br>
    • Answer: After repayment of loans or exit from equity investments, companies often maintain ongoing relationships with SBICs for follow-on funding, networking, and guidance for future growth.
    </p>
    <p><u><b>11. Are there any risks associated with SBIC funding?</u></b><br>
    • Answer: Risks include equity dilution if ownership is taken, interest payments on debt, potential loss of control in decision-making, and the obligation to meet covenants or reporting requirements.
    </p>
    <p><u><b>12. How does SBIC funding compare to other SBA programs or private investors?</u></b><br>
    • Answer: SBICs combine private sector management with SBA government leverage, offering larger funding amounts and longer-term capital than traditional SBA loans, while providing more structured mentorship and growth support than purely private investors.
    </p>
    <p><u><b>13. Can I apply for SBIC funding if I have already raised other capital?</u></b><br>
    • Answer: Yes, many SBICs accept companies that have existing private or public funding, but co-investment rules, preference rights, or reporting requirements may apply.
    </p>
    <p><u><b>14. What types of companies typically get approved by SBICs?</u></b><br>
    • Answer: Companies with high growth potential, scalable business models, strong management teams, and innovative products or services are most likely to be approved.
    </p>
    <p><u><b>15. How can I increase my chances of receiving SBIC funding?</u></b><br>
    • Answer: Prepare a solid business plan, demonstrate growth potential and market traction, have a capable management team, provide clear financials, and align your company with the SBIC's investment focus.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasbictwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBIC</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    SBA SBIC funding is suitable for early-growth to growth-stage businesses, typically those with proven products, steady revenue, and a need for capital to scale operations. Startups may participate if they have a solid business model and growth potential.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    Eligible entities include C-Corps, LLCs, and S-Corps. Sole proprietorships and partnerships may qualify in limited cases but are less common due to investor preferences for scalable corporate structures.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Businesses are generally expected to have some operational history and limited prior funding, demonstrating financial stability and growth potential. SBICs prefer companies that can leverage debt or equity to achieve significant expansion.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    SBIC investments operate through private equity and venture capital markets, backed by SBA guarantees. Previous funding rounds are considered but do not automatically disqualify a business.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    SBICs can provide moderate to large funding amounts, often ranging from $250,000 to several million dollars, depending on business size, growth stage, and financing needs.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    SBIC funding typically aligns with early-growth to expansion rounds, bridging the gap between traditional venture capital and bank financing. It can complement seed, Series A, or growth equity rounds.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Funding may be disbursed in single or multiple tranches, depending on the agreement and milestone achievement. SBICs may tie subsequent funding to operational or financial milestones.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Funds are generally flexible and may be used for:
    • Expansion and scaling operations
    • Marketing and sales growth
    • Hiring key personnel
    • Equipment or facility investment
    Restrictions are generally in place to ensure proper capital deployment aligned with growth objectives.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk is moderate, as SBICs provide debt or equity capital with government backing. Companies face operational, market, and repayment risks but benefit from SBA oversight and support.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Cost of capital may include equity dilution or interest on debt, depending on the SBIC structure. SBA guarantees can reduce borrowing costs and improve terms, making this financing more favorable than traditional private equity.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs can include legal fees, due diligence expenses, and compliance documentation, typically ranging from moderate to high, depending on transaction complexity.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    The SBIC application and funding process typically takes 2–6 months, depending on due diligence, investor evaluation, and SBA approval. Subsequent disbursements depend on milestone achievement.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
