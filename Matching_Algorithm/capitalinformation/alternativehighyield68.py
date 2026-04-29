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

def alternativehighyield(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Alternative</b></u><br>
    Capital Type: High Yield Business Consumer Loan </center></p>
    <p><b><u>Introduction</u></b><br>
High Yield Business Consumer Loans are ideal for businesses and individual borrowers seeking fast-access credit outside traditional banking channels, often to fund short-term needs, growth initiatives, or refinancing. They are designed so that capital is provided by alternative lenders at higher interest rates to compensate for elevated credit risk, limited collateral, or non-traditional borrower profiles. {n} fits that definition. In 2026, high-yield business consumer lending has expanded rapidly through fintech platforms, private credit funds, and specialty finance companies. These loans are commonly used by small businesses, sole proprietors, and consumers with limited access to bank credit, leveraging technology-driven underwriting models based on cash flow, transaction data, and behavioral analytics. While these loans provide speed and accessibility, they introduce high cost, default, and regulatory risk. Borrowers face elevated interest rates and fees, while lenders must manage credit performance, compliance obligations, and reputational exposure.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A High Yield Business Consumer Loan is a form of alternative credit extended to a business or individual borrower at above-market interest rates, reflecting increased credit risk, limited collateral, or non-traditional underwriting criteria. (Investopedia, 2025)
<br>


    <br>2.  High-yield business consumer loans occupy a position within the Private Credit segment of the capital markets, typically ranking as unsecured or lightly secured debt. In default scenarios, lenders rely primarily on borrower cash flows and contractual remedies rather than asset recovery. (Corporate Finance Institute, 2026)
<br>

    <br>3. Legally, these loans are governed by Loan Agreements or Consumer Credit Contracts that define interest rates, repayment schedules, fees, default provisions, and lender remedies. Structures must comply with applicable consumer protection, disclosure, and usury regulations. (Consumer Financial Protection Bureau, 2025)
<br>
    <br>4.From a risk perspective, high-yield business consumer loans expose lenders to elevated default, fraud, and macroeconomic sensitivity, while borrowers face affordability and refinancing risk due to high effective annualized costs. Portfolio diversification and data-driven underwriting are critical to risk management. (Federal Reserve Bank of New York, 2025)
<br>
    <br>5.
From an accounting and process standpoint, high-yield business consumer loans are recorded as Loan Receivables by lenders and Short-Term or Long-Term Liabilities by borrowers. Fintech-driven origination enables rapid funding, but requires ongoing servicing, collections, and regulatory reporting infrastructure. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). High-Interest Loans and Credit Risk. <a href="https://www.investopedia.com">https://www.investopedia.com</a>
<br>
    <br>Corporate Finance Institute (CFI). (2026). Alternative Lending and Private Credit. <a href="https://corporatefinanceinstitute.com/resources/credit-analysis">https://corporatefinanceinstitute.com/resources/credit-analysis</a>
<br>
    <br>Consumer Financial Protection Bureau (CFPB). (2025). Consumer Credit Regulations and Disclosures. <a href="https://www.consumerfinance.gov">https://www.consumerfinance.gov</a>
<br>
    <br>Federal Reserve Bank of New York. (2025). Household and Small Business Credit Trends. <a href="https://www.newyorkfed.org">https://www.newyorkfed.org</a>
<br>
    <br>Deloitte. (2025). Accounting and Risk Management for Alternative Lending. <a href="https://www2.deloitte.com/alternative-lending">https://www2.deloitte.com/alternative-lending</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Borrower Eligibility - Business entity or consumer borrower
<br>•   Credit Assessment - Cash flow, income, or alternative data underwriting
<br>•   Interest & Fee Disclosure - APR, fees, and repayment terms
<br>•   Regulatory Compliance - Consumer protection and lending laws
<br>•   Usury Limits - Jurisdictional interest rate caps
<br>•   AML & KYC Checks - Identity and fraud verification
<br>•   Data Privacy Compliance - Use of borrower data
<br>•   Collection Practices - Fair debt collection standards


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Loan Agreement / Credit Contract - Primary lending document
<br>•   Disclosure Statements - APR and fee disclosures
<br>•   Borrower Application - Financial and identity information
<br>•   Credit Assessment Reports - Underwriting analysis
<br>•   Payment Schedule - Repayment terms
<br>•   Compliance Certifications - Regulatory adherence
<br>•   Servicing & Collections Policies - Loan management procedures
<br>•   Board or Credit Committee Approvals - Lending authorization

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def alternativehighyieldfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Alternative<br>
    High Yield Business Consumer Loan</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a high-yield business consumer loan?</u></b><br>
    •Answer: A high-yield business consumer loan is a form of alternative credit that offers higher interest returns to lenders in exchange for lending to higher-risk business or consumer borrowers.
</p>

    <p><u><b>2. Who provides high-yield business consumer loans?</u></b><br>
    •Answer: These loans are typically provided by alternative lenders, fintech platforms, private credit funds, or peer-to-peer lending platforms.
</p>

    <p><u><b>3. Who are the typical borrowers of high-yield business consumer loans?</u></b><br>
    •Answer: Borrowers include small businesses, startups, or consumers with limited credit history or higher risk profiles.
</p>

    <p><u><b>4. When are high-yield business consumer loans typically used?</u></b><br>
    •Answer: They are used for working capital, expansion, debt consolidation, personal expenses, or short-term liquidity needs.
</p>

    <p><u><b>5. How do high-yield business consumer loans work?</u></b><br>
    •Answer: Lenders provide capital at higher interest rates, and borrowers repay principal and interest over a fixed or structured repayment schedule.
</p>

    <p><u><b>6. Why do these loans offer high yields?</u></b><br>
    •Answer: Higher yields compensate lenders for increased default risk, limited collateral, and borrower credit uncertainty.
</p>

    <p><u><b>7. Are high-yield business consumer loans secured or unsecured?</u></b><br>
    •Answer: They may be secured or unsecured, depending on the borrower profile and lender requirements.
</p>

    <p><u><b>8. What is the typical tenure of high-yield business consumer loans?</u></b><br>
    •Answer: Tenure generally ranges from a few months to several years.
</p>

    <p><u><b>9. How are interest rates determined for these loans?</u></b><br>
    •Answer: Rates are based on borrower risk, creditworthiness, loan size, duration, and market conditions.
</p>

    <p><u><b>10. What are the benefits of high-yield business consumer loans for borrowers?</u></b><br>
    •Answer: Benefits include access to capital, flexible underwriting, and faster approval compared to traditional banks.
</p>

    <p><u><b>11. What are the risks for lenders providing these loans?</u></b><br>
    •Answer: Risks include higher default rates, limited recovery options, and economic sensitivity.
</p>

    <p><u><b>12. What are the risks for borrowers taking high-yield loans?</u></b><br>
    •Answer: Risks include high borrowing costs, cash flow pressure, and potential over-leverage.
</p>

    <p><u><b>13. How do high-yield business consumer loans differ from traditional bank loans?</u></b><br>
    •Answer: They are easier to access and faster but significantly more expensive and less standardized.
</p>

    <p><u><b>14. Who typically invests in high-yield business consumer loans?</u></b><br>
    •Answer: Investors include private credit funds, institutional investors, and yield-seeking individuals.
</p>

    <p><u><b>15. When should high-yield business consumer loans be considered?</u></b><br>
    •Answer: They should be considered when access to traditional financing is limited and the borrower can manage higher repayment costs.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def alternativehighyieldtwelve(request):
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
    Capital Type: High Yield Business Consumer Loan</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
High yield business and consumer loans are best suited for operating businesses or consumer-facing platforms that require immediate access to capital and may not qualify for traditional bank financing. These loans are typically used by early revenue through mature-stage businesses rather than early-stage startups, as repayment capacity and cash flow visibility are critical.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
C-Corporations and LLCs are the most common entity types for high yield business loans, while consumer loans are typically extended to individuals or sole proprietors through regulated lending structures. For business use, formally registered entities are preferred due to enforceable repayment terms and underwriting requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Borrowers may have limited or significant prior capital, but eligibility is primarily driven by cash flow, credit profile, and income stability rather than capitalization. These loans are often used by borrowers with constrained access to bank credit or lower credit scores.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
High yield business and consumer loans operate within the alternative lending and non-bank finance market. Providers include private lenders, fintech platforms, specialty finance companies, and institutional investors seeking higher returns in exchange for elevated credit risk.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Loan sizes typically range from a few thousand dollars to several hundred thousand dollars for consumer loans and from tens of thousands to several million dollars for business loans. Capital availability is driven by underwriting limits, repayment capacity, and risk tolerance.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
These loans are not capital rounds and do not involve equity issuance. They are structured as standalone debt facilities with defined repayment schedules and interest obligations.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are most commonly disbursed in a single lump sum at closing. In some cases, revolving or repeat borrowing structures may be available based on borrower performance and repayment history.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Proceeds are typically used for short-term liquidity needs, working capital, inventory purchases, debt consolidation, emergency expenses, or personal consumption in the case of consumer loans. Use of funds is generally unrestricted.
<br>•   Working capital and inventory
<br>•   Debt consolidation
<br>•   Emergency expenses
<br>•   Short-term liquidity gaps

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk to lenders is high due to elevated default probability, while borrowers face repayment pressure from high interest rates, fees, and short maturities. For businesses, over-reliance on high-cost debt can strain cash flow and limit long-term growth.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is high and includes elevated interest rates, origination fees, service charges, and potential penalties. Effective annualized costs can be significantly higher than traditional bank loans.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are typically low to moderate and may include origination fees, underwriting charges, and administrative costs. Many fees are embedded into the loan structure rather than paid separately at closing.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is fast, often ranging from a few days to two weeks, making high yield loans attractive when speed and access outweigh cost considerations.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
