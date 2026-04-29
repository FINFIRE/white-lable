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

def smallbusinessadministrationsbasbaexpress(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Small Business Administration (SBA)</b></u><br>
    Capital Type: SBA Express </center></p>
    <p><b><u>Introduction</u></b><br>
    SBA Express loans are a streamlined loan program offered under the U.S. Small Business Administration (SBA) framework to provide faster access to working capital and expansion financing for small businesses. The program is designed to reduce approval time while maintaining SBA's partial loan guarantee to lenders. {n} fits that definition. The SBA Express program allows eligible small businesses to obtain financing more quickly than standard SBA 7(a) loans, with the SBA guaranteeing up to 50% of the loan amount. According to the U.S. Small Business Administration, SBA Express loans are commonly used for working capital, equipment purchases, revolving lines of credit, and business expansion due to their simplified documentation and expedited processing. While SBA Express loans offer speed and flexibility, they typically carry lower guarantee percentages and slightly higher interest rates than traditional SBA-backed loans.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. SBA Express loans are government-backed small business loans provided by SBA-approved lenders, with a reduced SBA guarantee designed to accelerate loan approval and disbursement. Under this program, lenders receive an SBA guarantee of up to 50% on loans of up to USD 500,000, enabling them to make faster credit decisions while reducing risk exposure. SBA Express loans can be structured as term loans or revolving lines of credit and are intended to support short- to medium-term business financing needs (U.S. SBA, n.d.).<br>
    <br>
    2. SBA Express loans are best suited for established small businesses that require quick access to capital and have stable cash flows, acceptable credit histories, and demonstrated repayment capacity. These loans are commonly used by service businesses, retail firms, professional practices, and small manufacturers seeking working capital, inventory financing, equipment acquisition, or short-term expansion funding. Compared to standard SBA 7(a) loans, SBA Express loans are particularly attractive to businesses that value speed over maximum loan guarantees. Companies that already maintain relationships with SBA-approved lenders tend to benefit most from this financing option (SBA, n.d.).<br>
    <br>
    3. The SBA Express program was introduced as part of broader SBA reforms aimed at improving access to credit for small businesses by reducing administrative delays and lender burden. Recognizing that lengthy approval processes discouraged both borrowers and lenders, the SBA developed Express loan products to increase participation by private lenders. Over time, SBA Express loans have become an important component of SBA's small business financing portfolio, particularly for working capital and revolving credit needs. The program complements traditional SBA 7(a) loans by offering a faster, more flexible alternative for qualifying businesses (GAO, 2020).<br>
    <br>
    4. Despite their advantages, SBA Express loans involve certain limitations. The SBA guarantee is capped at 50%, which increases lender risk and may result in higher interest rates or stricter credit requirements for borrowers. Loan amounts are also lower compared to standard SBA 7(a) loans, limiting suitability for capital-intensive projects. Additionally, borrowers are still personally liable for repayment, and personal guarantees are typically required. Failure to meet repayment obligations may negatively affect personal credit and business operations. These loans may not be appropriate for startups with limited operating history or inconsistent cash flows (OECD, 2021).<br>
    <br>
    5. To obtain an SBA Express loan, a business must apply through an SBA-approved Express lender. The lender conducts credit evaluation, cash-flow analysis, and due diligence, while the SBA provides a rapid eligibility response—often within 36 hours. Applicants must demonstrate business viability, repayment capacity, and compliance with SBA size and eligibility standards. Once approved, loan funds are disbursed directly by the lender. Borrowers are required to comply with loan covenants, reporting obligations, and repayment schedules throughout the loan term (U.S. SBA, n.d.).
    </p>
    <p><u><b>References</b></u><br>
    U.S. Small Business Administration. (n.d.). Loan guarantee programs. https://www.sba.gov<br>
    U.S. Small Business Administration. (n.d.). Types of SBA loans. https://www.sba.gov/funding-programs/loans<br>
    U.S. Government Accountability Office (GAO). (2020). Small business lending and SBA programs. https://www.gao.gov<br>
    OECD. (2021). Financing SMEs and entrepreneurs. https://www.oecd.org<br>
    U.S. Small Business Administration (SBA). (n.d.). Apply for an SBA loan. https://www.sba.gov/funding-programs/loans
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Business must meet SBA size standards<br>
    · Legally registered and operating business<br>
    · Acceptable credit history of owners<br>
    · Ability to provide personal guarantees<br>
    · Compliance with SBA eligibility rules<br>
    · No unresolved federal debt or legal violations
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · SBA Express loan application<br>
    · Business registration and licenses<br>
    · Business and personal tax returns<br>
    · Financial statements and cash-flow projections<br>
    · Personal financial statements of owners<br>
    · Bank statements<br>
    · Business plan or use-of-funds summary
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasbaexpressfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Small Business Administration (SBA)<br>
    SBA Express</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is the SBA Express loan program?</u></b><br>
    • Answer: SBA Express is a streamlined loan program under the U.S. Small Business Administration's 7(a) framework. It is designed to provide small businesses with faster access to capital through approved lenders, with reduced paperwork and quicker decision times compared to standard SBA loans.
    </p>
    <p><u><b>2. How does SBA Express differ from standard SBA 7(a) loans?</u></b><br>
    • Answer: SBA Express offers faster approval and less documentation but comes with a lower SBA guarantee percentage than standard 7(a) loans. This trade-off allows lenders to process loans more quickly while still benefiting from partial government backing.
    </p>
    <p><u><b>3. Who is eligible for SBA Express loans?</u></b><br>
    • Answer: Eligible applicants include U.S.-based small businesses that meet SBA size standards, operate for profit, and demonstrate the ability to repay the loan. Startups and existing businesses may qualify, subject to lender underwriting.
    </p>
    <p><u><b>4. What types of businesses are best suited for SBA Express?</u></b><br>
    • Answer: SBA Express is best suited for small businesses that need quick access to working capital, equipment financing, or short-term growth funding and can meet basic credit and cash-flow requirements.
    </p>
    <p><u><b>5. How much funding can a business receive through SBA Express?</u></b><br>
    • Answer: SBA Express loans offer smaller loan amounts than standard SBA 7(a) loans. The exact amount depends on lender policies, borrower qualifications, and SBA program limits.
    </p>
    <p><u><b>6. How quickly can funds be accessed?</u></b><br>
    • Answer: One of the key advantages of SBA Express is speed. Lenders can receive an SBA response in a short timeframe, allowing businesses to access funds significantly faster than traditional SBA loan processes.
    </p>
    <p><u><b>7. Does SBA Express require equity dilution?</u></b><br>
    • Answer: No. SBA Express is a debt-based financing option. Business owners retain full ownership and control of their company.
    </p>
    <p><u><b>8. Are personal guarantees or collateral required?</u></b><br>
    • Answer: Yes, personal guarantees are typically required from owners. Collateral requirements vary by lender and loan size, but SBA Express is generally more flexible than traditional bank loans.
    </p>
    <p><u><b>9. What can SBA Express loan funds be used for?</u></b><br>
    • Answer: Funds can be used for working capital, equipment purchase, inventory, refinancing certain debts, or other eligible business purposes under SBA guidelines.
    </p>
    <p><u><b>10. What are the interest rates and repayment terms?</u></b><br>
    • Answer: Interest rates are set by lenders within SBA-approved limits and are usually variable. Repayment terms depend on the use of funds, such as shorter terms for working capital and longer terms for equipment or real estate.
    </p>
    <p><u><b>11. What are the key benefits of SBA Express loans?</u></b><br>
    • Answer: Key benefits include faster approval times, reduced paperwork, government-backed risk reduction, no equity dilution, and flexibility in fund usage.
    </p>
    <p><u><b>12. What are the risks or limitations of SBA Express loans?</u></b><br>
    • Answer: Limitations include smaller loan amounts, partial (not full) SBA guarantees, repayment obligations regardless of business performance, and potential personal liability.
    </p>
    <p><u><b>13. Can SBA Express loans be combined with other funding sources?</u></b><br>
    • Answer: Yes. SBA Express loans can be combined with personal savings, grants, accelerators, or other debt or equity financing, subject to lender approval.
    </p>
    <p><u><b>14. How does SBA Express compare to SBA Veteran programs?</u></b><br>
    • Answer: SBA Express focuses on speed and convenience, while SBA Veteran programs add specialized training, counseling, and contracting support. Eligible veterans may benefit from fee reductions under SBA Express.
    </p>
    <p><u><b>15. How can businesses improve their chances of SBA Express approval?</u></b><br>
    • Answer: Businesses can improve approval odds by maintaining good personal and business credit, preparing clear financial statements, demonstrating repayment ability, and working with SBA-preferred lenders.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def smallbusinessadministrationsbasbaexpresstwelve(request):
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
    Capital Type: SBA Express</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    SBA Express loans are best suited for early-stage to established small businesses that have begun operations and can demonstrate basic revenue or cash-flow potential. While startups may qualify, the program is more commonly used by operating businesses seeking quick access to capital.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    SBA Express loans are available to most for-profit business entities, including sole proprietorships, partnerships, LLCs, and corporations. Businesses must meet SBA size standards and operate legally within eligible industries.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Applicants are expected to show owner investment and financial commitment. Prior funding—whether from personal savings, loans, or investors—is acceptable, as long as the business demonstrates the ability to service additional debt.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    SBA Express financing operates strictly as debt financing. Prior equity investments do not disqualify applicants, but lenders will evaluate the overall capital structure to ensure sustainable repayment capacity.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    SBA Express loans provide funding up to $500,000 (with SBA guaranteeing a portion of the loan). This makes them suitable for small to moderate capital needs, such as working capital, equipment purchases, or short-term expansion.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    SBA Express loans do not align with startup funding rounds. Instead, they fit into operational financing stages, supporting business launch, growth, or stabilization rather than venture-style scaling.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funds are typically disbursed in a single lump sum after approval. In some cases, the loan may be structured as a revolving line of credit, allowing ongoing access to capital as needed.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Approved uses include:<br>
    · Working capital<br>
    · Equipment and inventory<br>
    · Marketing and expansion activities<br>
    · Refinancing certain existing business debts<br>
    Use of funds for personal expenses or prohibited activities is not allowed.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk is moderate, as borrowers remain fully responsible for repayment. Personal guarantees are commonly required, exposing personal assets in the event of default.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    The cost of capital is moderate, including interest rates set by lenders and SBA guarantee fees. While rates are competitive, they are typically higher than standard SBA 7(a) loans due to the faster approval process.
    </p>
    <p><b><u>11 - Upfront Cost Assessment</u></b><br>
    Upfront costs may include origination fees, SBA guarantee fees, legal fees, and closing costs. These are generally lower than conventional loans but higher than personal funding sources.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    SBA Express is designed for speed, with lender decisions often made within 36 hours, and funding typically available within 2–4 weeks, depending on documentation and closing requirements.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
