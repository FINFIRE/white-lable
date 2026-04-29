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

def ownerdebtpersonalresourcesorloans(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Owner Debt</b></u><br>
    Capital Type: Personal Resources or Loans </center></p>
    <p><b><u>Introduction</u></b><br>
    Personal Resources or Loans are ideal for founders seeking maximum control and minimal outside interference during the earliest stages of a business. They are designed so that entrepreneurs can use their own savings, home equity, or personal bank credit to provide the initial "spark" of capital required for product development or market testing. {n} fits that definition. "Self-funding" or "bootstrapping" remains the most common way to start a business in America. In 2024, data from the Kauffman Foundation suggested that over 65% of startups began with personal savings as their primary source of capital. For example, iconic companies like Spanx, where Sara Blakely used $5,000 of her personal savings, show that small personal injections can lead to billion-dollar valuations. On average, founders using personal resources invest between $10,000 and $75,000 to launch, often utilizing a mix of cash and personal credit. While personal resources offer "non-dilutive" capital (you keep 100% of the equity), the risk of total personal financial ruin and the "opportunity cost" of spending retirement or emergency savings make this a high-stakes strategy that requires a disciplined budget.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Personal Resources or Loans refer to capital provided directly by the owner through personal liquid assets (cash, stocks, bonds) or personal credit facilities (Home Equity Lines of Credit, personal term loans). Unlike venture capital or business loans, this capital is not tied to the company's performance but rather to the owner's personal balance sheet. (Investopedia, 2025)<br><br>
    2. The best type of companies to fund via personal resources are low-overhead startups, service-based businesses, or "lean" technology firms that can reach a "break-even" point quickly. It is particularly effective for founders who want to retain total decision-making power and who do not yet have the "traction" required to attract institutional investors or traditional commercial bank loans. (Small Business Trends, 2025)<br><br>
    3. Bootstrapping emerged as a formalized business philosophy in the late 20th century, though it has been the default mode of commerce for millennia. The modern era of "lean startup" methodology (popularized in the 2010s) turned personal resource funding into a badge of honor, emphasizing "customer-funded growth" where personal savings are used only to get the first sale. In 2025, with the rise of high-interest rates, "internal funding" from personal sources has seen a massive resurgence as a way to avoid expensive debt. (Harvard Business Review, 2024)<br><br>
    4. While personal funding offers freedom, it carries significant "concentration" risk. If the business fails, the founder loses not just their job, but their personal safety net. Furthermore, using personal loans like a HELOC (Home Equity Line of Credit) puts the owner's primary residence at risk. There is also the "scaling ceiling"—businesses funded purely by personal resources often grow much slower than those with external "rocket fuel" from VCs or SBA loans. (Entrepreneur.com, 2024)<br><br>
    5. To leverage personal resources effectively, a founder must maintain a strict "firewall" between personal and business accounting. This is usually done by "loaning" the money to the business via a formal Promissory Note, which allows the owner to be repaid with interest as the company becomes profitable. This structure protects the owner's legal standing and ensures that the capital is treated as a professional investment rather than a "hobbyist" expense. (Nolo, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Investopedia. (2025, Jan 02). Bootstrapping Definition: Strategies and Pros & Cons. https://www.investopedia.com/terms/b/bootstrapping.asp<br>
    Small Business Trends. (2025, March 14). How to Self-Fund Your Startup: A Practical Guide. https://smallbiztrends.com/<br>
    Harvard Business Review. (2024). The Art of the Bootstrapper. https://hbr.org/<br>
    Entrepreneur.com. (2024, Dec 11). Why Personal Savings is Still the Best Way to Fund Your Business. https://www.entrepreneur.com/starting-a-business/how-to-fund-your-business-using-personal-savings/441238<br>
    Nolo. (2025). Documenting Your Investment in Your Own Business. https://www.nolo.com/legal-encyclopedia/using-your-own-money-to-start-a-business.html
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Clear Chain of Title – Proof that personal funds were legally obtained (to comply with Anti-Money Laundering/AML laws).<br>
    • Promissory Note – If the money is a loan to the company, a written agreement must exist specifying interest and term.<br>
    • Solvency of the Individual – For personal bank loans, a Debt-to-Income (DTI) ratio typically below 36% to 43%.<br>
    • Minimum Credit Score – For personal loans/HELOCs, usually requires a score of 680 or higher.<br>
    • Equity Documentation – If the funds are a "capital contribution," they must be recorded in the company's Ledger or Cap Table.<br>
    • UCC-1 Filing – (Optional) If the owner wants to be a "secured creditor" of their own company to protect their personal loan in a bankruptcy.<br>
    • No Commingling – Legally, funds must be transferred to a dedicated business bank account before being spent.
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • Personal Bank Statements – Showing the availability of liquid cash.<br>
    • Home Equity Statement – (If using a HELOC) Showing available equity in real estate.<br>
    • Promissory Note – The legal contract between the owner (Lender) and the Business (Borrower).<br>
    • Capital Contribution Agreement – (If an equity injection) Outlining the shares issued for the cash.<br>
    • Personal Financial Statement (PFS) – A snapshot of the owner's assets and liabilities.<br>
    • Personal Tax Returns – Last 2 years (usually required by banks if getting a personal loan for business).<br>
    • Budget/Use of Funds – A breakdown of exactly how the personal cash will be spent.
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def ownerdebtpersonalresourcesorloansfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Owner Debt<br>
    Personal Resources or Loans</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is owner debt through personal resources or loans?</u></b><br>
    • Answer: Owner debt through personal resources or loans occurs when a business owner uses personal savings, personal loans, or borrowed funds in their own name to finance business operations, making the owner personally liable for repayment.
    </p>
    <p><u><b>2. What types of businesses commonly rely on owner personal resources or loans?</u></b><br>
    • Answer: Startups, sole proprietorships, and early-stage small businesses with limited access to institutional financing commonly rely on owner personal resources or loans.
    </p>
    <p><u><b>3. How much funding can be provided through personal resources or loans?</u></b><br>
    • Answer: Funding amounts depend on the owner's personal savings, credit profile, and borrowing capacity, typically ranging from a few thousand dollars to several hundred thousand dollars.
    </p>
    <p><u><b>4. How quickly can funds be accessed through owner personal resources or loans?</u></b><br>
    • Answer: Personal savings can be accessed immediately, while personal loans usually provide funding within a few days to a few weeks after approval.
    </p>
    <p><u><b>5. What are the typical interest rates for personal loans used as owner debt?</u></b><br>
    • Answer: Interest rates vary based on creditworthiness and lender type, generally ranging from moderate to high compared to business loans.
    </p>
    <p><u><b>6. Is collateral required for personal loans used as owner debt?</u></b><br>
    • Answer: Some personal loans are unsecured, while others may require collateral such as personal assets, depending on the lender and loan size.
    </p>
    <p><u><b>7. Does using personal resources or loans affect personal credit?</u></b><br>
    • Answer: Yes, personal loans and repayment behavior directly impact the owner's personal credit score and overall financial health.
    </p>
    <p><u><b>8. Can owner personal loans be used for any business purpose?</u></b><br>
    • Answer: Yes, funds can generally be used for most business expenses including startup costs, working capital, equipment, or marketing.
    </p>
    <p><u><b>9. What are the main advantages of using owner personal resources or loans?</u></b><br>
    • Answer: Advantages include fast access to capital, full ownership retention, flexibility in use of funds, and minimal business qualification requirements.
    </p>
    <p><u><b>10. What are the risks associated with owner personal resources or loans?</u></b><br>
    • Answer: Risks include personal financial exposure, repayment pressure regardless of business performance, and potential loss of personal assets.
    </p>
    <p><u><b>11. Can owner debt from personal resources be combined with other funding sources?</u></b><br>
    • Answer: Yes, it is commonly combined with bank loans, SBA financing, grants, or equity investments to strengthen overall capital structure.
    </p>
    <p><u><b>12. How does owner personal debt compare to external business debt?</u></b><br>
    • Answer: Owner personal debt is easier to obtain but riskier for the owner, while external business debt may offer better terms with reduced personal exposure.
    </p>
    <p><u><b>13. Are there tax considerations when using personal resources or loans for business?</u></b><br>
    • Answer: Interest may or may not be deductible depending on how funds are structured and documented, so proper accounting and tax advice are recommended.
    </p>
    <p><u><b>14. Is owner debt through personal resources suitable for long-term financing?</u></b><br>
    • Answer: It is generally better suited for short-term or bridge financing rather than long-term capital needs due to personal risk and repayment constraints.
    </p>
    <p><u><b>15. How can owners reduce risk when using personal resources or loans?</u></b><br>
    • Answer: Owners can reduce risk by limiting exposure, maintaining clear documentation, refinancing into business debt when possible, and ensuring realistic cash flow planning.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def ownerdebtpersonalresourcesorloanstwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Owner Debt</b></u><br>
    Capital Type: Personal Resources or Loans</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Owner personal resources or loans are best suited for idea-stage to early-stage businesses, especially when external financing is unavailable. They are often used to launch operations or bridge short-term funding gaps.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    All entity types are eligible, including sole proprietorships, partnerships, LLCs, S-Corps, and C-Corps, as the capital originates from the owner personally rather than the business entity.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Availability depends on the owner's personal financial strength, including savings, income, credit access, or personal borrowing capacity. No business operating history is required.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    This financing is non-institutional and non-market-based, relying on personal funds or personal loans rather than banks, investors, or public markets.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Capital amounts are typically limited, constrained by personal financial capacity. It is suitable for small to moderate capital needs, not large-scale expansion.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    This capital source does not align with formal equity rounds. It is commonly used pre-seed or alongside early seed funding.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Funds may be contributed in a single tranche or multiple tranches, depending on cash availability or loan disbursement timing.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Funds are generally flexible and used for: Startup and formation costs; Initial operating expenses; Equipment, inventory, or marketing. Proper documentation is recommended to distinguish owner loans from equity.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk is high, as the owner's personal finances are directly exposed. Business failure may result in personal financial loss or increased debt burden.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    Capital cost includes opportunity cost of personal savings or interest on personal loans. There is no equity dilution, but personal financial strain may occur.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are generally low, limited to loan origination fees (if applicable) or minimal administrative expenses.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing is typically very fast, with funds available immediately or within days, depending on access to personal resources or loan approval speed.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
