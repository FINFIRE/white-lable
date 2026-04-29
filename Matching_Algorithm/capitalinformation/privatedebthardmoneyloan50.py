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

def privatedebthardmoneyloan(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Hard Money Loan </center></p>
    <p><b><u>Introduction</u></b><br>
A Hard Money Loan is ideal for borrowers that require short-term, asset-backed financing and are unable or unwilling to access traditional bank lending due to speed, credit constraints, or unconventional deal structures. It is designed so that capital is provided by private lenders based primarily on the value of collateral—most commonly real estate—rather than the borrower's creditworthiness or cash flow profile. {n} fits that definition. In 2026, hard money loans continue to play a critical role in real estate transactions, bridge financing, distressed asset acquisitions, and time-sensitive opportunities. These loans are commonly used by property investors, developers, and special-purpose vehicles for fix-and-flip projects, land acquisitions, and transitional assets. Private lenders and debt funds dominate this market due to their ability to underwrite and close deals rapidly. While hard money loans offer speed and flexibility, they carry elevated cost and default risk. Interest rates and fees are materially higher than conventional debt, and loan terms are short. Failure to refinance or exit on time can result in foreclosure or forced asset sales, making risk management and exit planning essential.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Hard Money Loan is a form of private, short-term debt secured by tangible assets—typically real estate—where lending decisions are driven primarily by collateral value and loan-to-value (LTV) ratios rather than borrower income or credit history. (Investopedia, 2025)
<br>


    <br>2.  Hard money loans occupy a senior position within the Capital Stack, usually as first-lien secured debt. In the event of default or liquidation, hard money lenders have priority claims over the pledged collateral, giving them strong downside protection. (Corporate Finance Institute, 2026)
<br>

    <br>3. Legally, hard money loans are governed by a Loan Agreement and secured through instruments such as mortgages, deeds of trust, or security agreements that grant the lender foreclosure rights upon default. These loans often include interest-only payments, balloon maturities, and aggressive default remedies. (Nolo, 2025)
<br>

    <br>4.From a risk perspective, hard money loans shift underwriting risk away from borrower credit and toward asset valuation and market liquidity risk. Borrowers face elevated refinancing and execution risk, while lenders rely on collateral enforceability and exit timelines to manage downside exposure. (Moody's Analytics, 2025)
<br>

    <br>5.
From an accounting and process standpoint, hard money loans are recorded as Short-Term or Long-Term Liabilities depending on maturity, with interest expense and origination fees amortized over the loan term. Due to simplified underwriting and limited documentation, these loans can close within days rather than months. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia. (2025). Hard Money Loan Definition and Uses. <a href="https://www.investopedia.com/hard-money-loan">https://www.investopedia.com/hard-money-loan</a>
<br>

    <br>Corporate Finance Institute (CFI). (2026). Private Debt and Asset-Based Lending. <a href="https://corporatefinanceinstitute.com/resources/credit-analysis">https://corporatefinanceinstitute.com/resources/credit-analysis</a>
<br>

    <br>Nolo. (2025). Hard Money Lending and Foreclosure Law. <a href="https://www.nolo.com/hard-money-loans">https://www.nolo.com/hard-money-loans</a>
<br>

    <br>Moody's Analytics. (2025). Risk Considerations in Asset-Based Lending. <a href="https://www.moodysanalytics.com">https://www.moodysanalytics.com</a>
<br>

    <br>Deloitte. (2025). Accounting for Short-Term and Asset-Backed Debt. <a href="https://www2.deloitte.com/debt-accounting">https://www2.deloitte.com/debt-accounting</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Borrower Eligibility – Individual, SPV, or operating entity
<br>•   Defined Use of Proceeds – Property acquisition, renovation, or bridge financing
<br>•   Collateral Valuation – Appraisal or broker price opinion (BPO)
<br>•   Loan-to-Value (LTV) Limits – Typically 50%–70%
<br>•   Security Instruments – Mortgage, deed of trust, or lien filing
<br>•   Interest & Fee Disclosure – Rates, points, and penalties
<br>•   Default & Foreclosure Terms – Enforcement and remedies
<br>•   Regulatory Compliance – State lending and usury laws


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Loan Agreement – Primary debt contract
<br>•   Promissory Note – Borrower repayment obligation
<br>•   Mortgage / Deed of Trust – Collateral security instrument
<br>•   Appraisal or BPO – Asset valuation report
<br>•   Title Report & Insurance – Lien priority confirmation
<br>•   Draw Schedule (if applicable) – Construction or rehab funding
<br>•   Exit Strategy Plan – Refinance or sale pathway
<br>•   Borrower Resolutions – Authorization to incur debt

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebthardmoneyloanfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Hard Money Loan</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a hard money loan?</u></b><br>
    •Answer: A hard money loan is a short-term, asset-backed private debt loan provided by private lenders, primarily secured by real estate rather than the borrower's creditworthiness.
</p>

    <p><u><b>2. Who typically provides hard money loans?</u></b><br>
    •Answer: Hard money loans are usually provided by private individuals, private lending firms, or non-bank financial institutions.
</p>

    <p><u><b>3. When are hard money loans typically used?</u></b><br>
    •Answer: Hard money loans are commonly used for real estate acquisitions, bridge financing, renovations, or situations requiring fast access to capital.
</p>

    <p><u><b>4. What type of collateral is required for a hard money loan?</u></b><br>
    •Answer: Hard money loans are secured by tangible assets, most commonly real estate, which serves as collateral.
</p>

    <p><u><b>5. How does a hard money loan work?</u></b><br>
    •Answer: The lender provides funds based on the value of the collateral, and the borrower repays the loan with interest over a short term, often with a balloon payment.
</p>

    <p><u><b>6. What is the typical loan-to-value (LTV) ratio for hard money loans?</u></b><br>
    •Answer: Hard money lenders typically offer loans with LTV ratios ranging from 50% to 70% of the property's value.
</p>

    <p><u><b>7. What are the interest rates on hard money loans?</u></b><br>
    •Answer: Interest rates are higher than traditional loans, commonly ranging from 8% to 15% or more, reflecting higher risk.
</p>

    <p><u><b>8. What is the typical term of a hard money loan?</u></b><br>
    •Answer: Hard money loans are short-term, usually ranging from 6 months to 3 years.
</p>

    <p><u><b>9. How quickly can a hard money loan be funded?</u></b><br>
    •Answer: Hard money loans can often be approved and funded within days or weeks, much faster than traditional bank loans.
</p>

    <p><u><b>10. Are credit scores important for hard money loans?</u></b><br>
    •Answer: Credit scores are less important; lenders focus primarily on the value of the collateral and the exit strategy.
</p>

    <p><u><b>11. What fees are associated with hard money loans?</u></b><br>
    •Answer: Fees often include origination fees, closing costs, and "points," which are upfront fees calculated as a percentage of the loan amount.
</p>

    <p><u><b>12. What are the risks of hard money loans for borrowers?</u></b><br>
    •Answer: Risks include high interest rates, short repayment periods, and potential loss of collateral if the loan defaults.
</p>

    <p><u><b>13. What are the benefits of hard money loans?</u></b><br>
    •Answer: Benefits include fast access to capital, flexible underwriting, and availability for borrowers who may not qualify for traditional loans.
</p>

    <p><u><b>14. Can hard money loans be refinanced?</u></b><br>
    •Answer: Yes, borrowers often refinance hard money loans with traditional financing once the property is stabilized or improved.
</p>

    <p><u><b>15. When should a borrower consider a hard money loan?</u></b><br>
    •Answer: A borrower should consider a hard money loan when speed is critical, traditional financing is unavailable, and a clear exit or refinancing plan exists.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebthardmoneyloantwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Debt</b></u><br>
    Capital Type: Hard Money Loan</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Hard money loans are best suited for asset-backed businesses or projects rather than traditional startup lifecycle stages. They are commonly used by early-stage through mature entities when rapid access to capital is required and a tangible asset, such as real estate or equipment, can be pledged as collateral. Company stage is less important than asset value and exit clarity.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
C-Corporations, LLCs, and special purpose vehicles are commonly used for hard money loans, as these structures allow clear collateral ownership and enforceable loan agreements. Sole proprietorships may be used in limited cases but are generally less preferred due to higher risk and weaker legal separation between the borrower and the asset.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Hard money loans can be accessed regardless of prior equity or debt history, provided sufficient collateral exists. Borrowers may have limited operating history, poor credit, or constrained access to traditional financing, as hard money lenders prioritize asset value and exit strategy over balance sheet strength.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Hard money loans operate within the private alternative lending market and are typically provided by private lenders, family offices, real estate-focused funds, and non-bank lenders. This market is designed for speed, flexibility, and asset-based underwriting rather than institutional credit analysis.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Loan amounts typically range from $50,000 to several million dollars, depending on the value of the underlying collateral and loan-to-value ratios. Capital availability is driven by asset quality, market liquidity, and the lender's risk tolerance rather than company valuation.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Hard money loans are not part of traditional fundraising rounds and are instead structured as standalone debt facilities tied to a specific asset or project. They are often used as bridge financing, acquisition financing, or short-term capital ahead of refinancing or asset sale.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are most commonly disbursed in a single tranche at closing. In some cases, staged disbursements may occur if the loan supports a development or renovation project, with releases tied to construction milestones or inspections.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Hard money loan proceeds are typically used for asset acquisition, bridge financing, property renovation, development costs, or urgent liquidity needs. Use of funds is usually restricted to purposes directly related to the collateral or project supporting the loan.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk for lenders is mitigated by collateral but remains elevated due to borrower credit profiles and market volatility. For borrowers, risk includes high interest rates, short maturities, strict default terms, and potential loss of the underlying asset if repayment or refinancing does not occur as planned.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital for hard money loans is high relative to traditional bank debt and includes elevated interest rates, origination fees, points, and sometimes prepayment penalties. These costs reflect the speed, flexibility, and higher risk assumed by private lenders.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate to high and may include origination fees, lender points, legal documentation, appraisal fees, inspections, and closing costs. These expenses are typically paid at closing and increase with loan complexity and asset valuation requirements.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is fast compared to traditional financing, often ranging from a few days to three weeks, making hard money loans a viable option when speed and certainty of execution are critical.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
