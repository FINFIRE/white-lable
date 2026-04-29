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

def alternativeapps(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Alternative</b></u><br>
    Capital Type: Apps (i.e. Kabbage) </center></p>
    <p><b><u>Introduction</u></b><br>
App-based lending—pioneered by platforms like Kabbage (now part of American Express)—is ideal for companies seeking immediate, short-term liquidity without the paperwork or wait times of a traditional bank. It is designed so that small businesses can sync their accounting or banking data directly to an algorithm that provides a credit decision in minutes. {n} fits that definition. In 2026, the alternative lending landscape is highly automated. Following the acquisition of Kabbage by American Express, the market shifted from standalone "fintech" apps to integrated "embedded finance" solutions. These platforms typically offer revolving lines of credit ranging from $2,000 to $250,000. While a bank might take 30 days to approve a loan, these apps can fund an account in as little as 24 hours. While the speed of app-based lending is unparalleled, the cost is significantly higher than traditional debt. Instead of simple interest, many use "factor rates" or "monthly fees" that can result in an Effective APR of 15% to 50%, making it a tool for quick-turn opportunities rather than long-term infrastructure.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.App-Based Lending is a form of digital credit where the underwriting is performed by an algorithm rather than a human loan officer. By connecting to your business's checking account, QuickBooks, or Amazon seller account, the lender analyzes real-time cash flow and transaction volume to determine risk. Unlike traditional loans, these are often "revolving," meaning you only pay for what you draw. (American Express, 2025)
<br>


    <br>2.  The best type of companies for these apps are retailers, e-commerce sellers, and service providers with high transaction volume but occasional cash flow gaps. It is perfect for "Inventory Spikes" (buying stock for the holidays) or "Bridge Gaps" (waiting for a large invoice to clear). Because the decision is data-driven, it is often accessible to businesses that have been operating for as little as 6 to 12 months. (Investopedia, 2026)
<br>

    <br>3. The market emerged around 2008-2010 as a reaction to banks cutting off small business credit during the financial crisis. Kabbage revolutionized the space by using "Alternative Data"—like social media engagement and shipping volume—to approve loans. By 2026, the technology has evolved into "Contextual Lending," where the loan offer is embedded directly into the software the business uses to run its operations (e.g., Shopify Capital or Square Loans). (Business Insider, 2025)
<br>
    <br>4.While the access is easy, it carries "Margin Erosion" risks. Because the repayments are often automated and taken daily or weekly, it can put a strain on daily operations if sales slow down. Additionally, these loans are often Short-Term (6-18 months). If a business uses this high-cost capital for a project that doesn't generate an immediate return, the interest payments can quickly consume all profit. (Forbes Advisor, 2025)
<br>
    <br>5.
To raise capital via these apps, a founder simply creates an account and "plugs in" their data sources. The lender performs a "Soft Credit Pull" initially (which doesn't hurt your score) to provide an estimated limit. Once you accept, the "Hard Pull" occurs, and the funds are digitally transferred. Most of these apps require a minimum of $3,000 to $10,000 in monthly revenue to qualify. (Bluevine, 2026)
    </p>

    <p><u><b>References</u></b><br>
    <br>American Express. (2025). Business Blueprint: Understanding Your Line of Credit. <a href="https://www.americanexpress.com/en-us/business/blueprint/">https://www.americanexpress.com/en-us/business/blueprint/</a>
<br>
    <br>Investopedia. (2026). Fintech Lending: How Algorithms Are Replacing Banks. <a href="https://www.investopedia.com/fintech-lending-overview">https://www.investopedia.com/fintech-lending-overview</a>
<br>
    <br>Forbes Advisor. (2025). Best Small Business Lines of Credit 2025. <a href="https://www.forbes.com/advisor/business-loans/best-business-lines-of-credit/">https://www.forbes.com/advisor/business-loans/best-business-lines-of-credit/</a>
<br>
    <br>Bluevine. (2026). Financing Solutions for Growing Businesses. <a href="https://www.bluevine.com/">https://www.bluevine.com/</a>
<br>
    <br>Business Insider. (2025). The Future of Embedded Finance in Small Business. <a href="https://www.businessinsider.com/embedded-finance-trends">https://www.businessinsider.com/embedded-finance-trends</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Minimum Time in Business - Usually 6 to 12 months of active operation
<br>•   Monthly Revenue Threshold - Typically requires $3k to $10k in verifiable monthly sales
<br>•   Business Bank Account - Must have a dedicated business checking account (personal accounts are usually rejected)
<br>•   FICO Score - Minimums are lower than banks (often 600+), but the rate you pay is highly dependent on this score
<br>•   Entity Type - Must be a registered LLC, S-Corp, C-Corp, or General Partnership
<br>•   Personal Guarantee - Most apps require a digital "Personal Guarantee" signed at the time of application


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Business Bank Account Connection - Usually via Plaid or similar API
<br>•   Accounting Software Sync - Connecting QuickBooks, Xero, or FreshBooks
<br>•   Tax ID Number (EIN) - For business identity verification
<br>•   Driver's License Scan - For "Know Your Customer" (KYC) identity checks
<br>•   Voided Check - To establish the Automated Clearing House (ACH) connection for withdrawals and repayments

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def alternativeappsfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Alternative<br>
    Apps (i.e. Kabbage)</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are alternative financing apps like Kabbage?</u></b><br>
    •Answer: Alternative financing apps are digital platforms that provide fast, short-term funding to small businesses using automated, data-driven credit assessments instead of traditional banking processes.
</p>

    <p><u><b>2. How do alternative financing apps work?</u></b><br>
    •Answer: These apps connect to business data sources such as bank accounts, payment processors, and accounting software to assess cash flow and approve funding quickly.
</p>

    <p><u><b>3. Who can use alternative financing apps?</u></b><br>
    •Answer: Small businesses, startups, freelancers, and self-employed individuals with consistent revenue but limited access to traditional bank loans commonly use these apps.
</p>

    <p><u><b>4. What types of funding do these apps provide?</u></b><br>
    •Answer: They typically offer lines of credit, short-term loans, invoice financing, and merchant cash advances.
</p>

    <p><u><b>5. How fast can I get funding through these apps?</u></b><br>
    •Answer: Funding is often approved within minutes to hours, with funds deposited as quickly as the same day or within 1-3 business days.
</p>

    <p><u><b>6. Do alternative financing apps require collateral?</u></b><br>
    •Answer: Most apps do not require traditional collateral, instead relying on cash flow data and business performance.
</p>

    <p><u><b>7. What are the interest rates or fees like?</u></b><br>
    •Answer: Rates and fees are generally higher than traditional bank loans due to increased risk and convenience, often structured as fixed fees or factor rates.
</p>

    <p><u><b>8. Is credit score important for these apps?</u></b><br>
    •Answer: Credit score is considered but usually less important than real-time business revenue and cash flow data.
</p>

    <p><u><b>9. Are these apps suitable for startups?</u></b><br>
    •Answer: They may suit revenue-generating startups, but pre-revenue or very early-stage startups may struggle to qualify.
</p>

    <p><u><b>10. Can I use alternative financing apps alongside bank loans?</u></b><br>
    •Answer: Yes, many businesses use these apps to supplement traditional financing, especially for short-term working capital needs.
</p>

    <p><u><b>11. What are the advantages of alternative financing apps?</u></b><br>
    •Answer: Advantages include speed, convenience, minimal paperwork, flexible access to capital, and online account management.
</p>

    <p><u><b>12. What are the disadvantages of using these apps?</u></b><br>
    •Answer: Disadvantages include higher costs, shorter repayment terms, and potential cash flow pressure due to frequent repayments.
</p>

    <p><u><b>13. How is repayment usually structured?</u></b><br>
    •Answer: Repayments are often automated and deducted daily, weekly, or monthly directly from the business bank account.
</p>

    <p><u><b>14. Do alternative financing apps impact business ownership?</u></b><br>
    •Answer: No, these apps provide debt financing and do not take equity in the business.
</p>

    <p><u><b>15. When should a business consider using alternative financing apps?</u></b><br>
    •Answer: Businesses should consider them when quick access to capital is needed, cash flow is predictable, and traditional financing is unavailable or too slow.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def alternativeappstwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Alternative</b></u><br>
    Capital Type: Apps (i.e. Kabbage)</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Alternative lending apps are best suited for operating small businesses with active revenue. These platforms typically require consistent cash flow, making them unsuitable for pre-revenue startups.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
These platforms generally support sole proprietorships, LLCs, S-Corps, and C-Corps. Eligibility is based more on bank account activity and revenue history than on corporate structure.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Businesses must demonstrate recent and recurring revenue, usually through linked bank accounts, payment processors, or accounting software. Existing debt is allowed, but overall cash flow health is assessed.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Alternative lending apps operate in the fintech private lending market, using automated underwriting rather than traditional credit committee processes.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Funding amounts are typically small to mid-sized, commonly ranging from $5,000 to $250,000, depending on revenue levels and transaction history.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
This capital is non-equity and non-round-based. It is designed for short-term liquidity, not long-term capital structuring.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Most platforms offer revolving lines of credit or short-term installment loans, allowing repeated access to capital as balances are repaid.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Permitted uses usually include:
<br>•   Working capital
<br>•   Payroll and operating expenses
<br>•   Inventory purchases
<br>•   Short-term cash flow gaps
Restrictions generally prohibit personal use or speculative investments.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to the borrower is moderate to high due to short repayment terms and automatic withdrawals from business accounts. Cash flow disruption is the primary risk.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is high compared to traditional loans, with pricing often expressed as factor rates, flat fees, or higher APR equivalents.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are typically low, with minimal documentation and no traditional closing costs. Fees are often embedded in repayment structures.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is very fast, often within days or even same-day funding, once accounts are linked and approved.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
