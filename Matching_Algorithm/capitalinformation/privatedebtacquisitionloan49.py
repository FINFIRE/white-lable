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
def privatedebtacquisitionloan(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Acquisition Loan </center></p>
    <p><b><u>Introduction</u></b><br>
An Acquisition Loan is ideal for companies, private equity sponsors, or holding vehicles seeking to finance the purchase of another business without issuing equity at the operating-company level. It is designed so that capital is provided as senior or subordinated debt specifically to fund mergers, acquisitions, or buyouts, with repayment driven by the acquired company's cash flows and assets. {n} fits that definition. In 2026, acquisition loans remain a cornerstone of the private debt and leveraged finance markets, particularly in lower-middle-market and middle-market transactions. These loans are commonly used in management buyouts (MBOs), sponsor-led acquisitions, platform roll-ups, and strategic bolt-on transactions. Private credit funds, direct lenders, and alternative asset managers have increasingly replaced traditional banks as the primary providers of acquisition financing due to speed, flexibility, and certainty of execution. While acquisition loans allow buyers to preserve equity and amplify returns, they introduce leverage and integration risk. Debt service obligations begin immediately post-close, and failure to achieve projected synergies or cash flow targets can strain liquidity. As a result, acquisition loans are heavily structured, covenant-driven, and supported by collateral, guarantees, and cash flow controls.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.An Acquisition Loan is a form of private debt issued to finance the purchase of a target company, where repayment is primarily supported by the cash flows, assets, and earnings of the acquired business rather than the borrower's standalone balance sheet. These loans are typically structured as term loans with fixed or floating interest rates. (Corporate Finance Institute, 2026)
<br>



    <br>2.  Acquisition loans occupy a defined position within the Capital Stack, most commonly as senior secured debt, though they may also include subordinated, mezzanine, or unitranche structures. In a liquidation scenario, lenders are repaid prior to equity holders and, in most cases, prior to unsecured creditors. (Moody's Investors Service, 2025)
<br>

    <br>3. Legally, acquisition loans are governed by a comprehensive Credit Agreement that outlines loan amount, interest rate, maturity, amortization, covenants, events of default, and remedies. These agreements are often accompanied by security documents granting liens over shares, assets, and cash flows of the acquired entity. (Latham & Watkins, 2025)
<br>

    <br>4.From a risk perspective, acquisition loans transfer ownership dilution risk away from the borrower while introducing leverage, refinancing, and execution risks. If post-acquisition performance underperforms projections, borrowers may face covenant breaches, accelerated repayment demands, or lender control rights. (S&P Global Ratings, 2025)
<br>

    <br>5.
From an accounting and process standpoint, acquisition loans are recorded as Long-Term Liabilities on the balance sheet, with interest expense flowing through the income statement. The loan process typically includes extensive due diligence, cash flow modeling, and lender approval, making acquisition loans slower to close than equity but significantly more capital-efficient. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>Corporate Finance Institute (CFI). (2026). Acquisition Financing and Leveraged Buyouts. <a href="https://corporatefinanceinstitute.com/resources/valuation/acquisition-financing">https://corporatefinanceinstitute.com/resources/valuation/acquisition-financing</a>
<br>

    <br>Moody's Investors Service. (2025). Private Credit and Acquisition Debt Structures. <a href="https://www.moodys.com/private-credit">https://www.moodys.com/private-credit</a>
<br>

    <br>Latham & Watkins. (2025). Acquisition Finance: Key Legal Considerations. <a href="https://www.lw.com/acquisition-finance">https://www.lw.com/acquisition-finance</a>
<br>

    <br>S&P Global Ratings. (2025). Leverage and Credit Risk in M&A Transactions. <a href="https://www.spglobal.com/ratings">https://www.spglobal.com/ratings</a>
<br>

    <br>Deloitte. (2025). Accounting for Acquisition-Related Debt. <a href="https://www2.deloitte.com/acquisition-accounting">https://www2.deloitte.com/acquisition-accounting</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Borrower Eligibility – Acquisition vehicle, sponsor-backed entity, or operating company
<br>•   Defined Acquisition Use – Funds restricted to approved transaction costs and purchase price
<br>•   Financial Covenants – Leverage, coverage, and liquidity ratios
<br>•   Security & Collateral – Liens over shares, assets, and cash flows
<br>•   Guarantees – Parent, sponsor, or operating-company guarantees
<br>•   Change-of-Control Provisions – Restrictions on ownership changes
<br>•   Regulatory Approvals – Antitrust, sector-specific, and jurisdictional clearances
<br>•   Lender Due Diligence – Legal, financial, tax, and operational review


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Credit Agreement – Primary loan contract
<br>•   Term Sheet – Key commercial and structural terms
<br>•   Security Agreement – Collateral and lien documentation
<br>•   Share Pledge Agreement – Pledge of equity interests
<br>•   Intercreditor Agreement – Priority and enforcement rights
<br>•   Financial Model – Post-acquisition cash flow projections
<br>•   Due Diligence Reports – Legal, financial, tax, and operational
<br>•   Board & Shareholder Resolutions – Transaction approvals

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtacquisitionloanfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Acquisition Loan</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a private debt acquisition loan?</u></b><br>
    •Answer: A private debt acquisition loan is financing provided by private lenders to acquire another business, asset, or controlling stake in a company.
</p>

    <p><u><b>2. Who typically provides private acquisition loans?</u></b><br>
    •Answer: These loans are commonly provided by private debt funds, family offices, hedge funds, or alternative lenders.
</p>

    <p><u><b>3. What types of acquisitions use private debt?</u></b><br>
    •Answer: Private debt acquisition loans are used for mergers, leveraged buyouts, management buyouts, and strategic acquisitions.
</p>

    <p><u><b>4. How much capital can be raised through a private acquisition loan?</u></b><br>
    •Answer: Loan amounts vary widely and can range from several million to hundreds of millions, depending on deal size and borrower profile.
</p>

    <p><u><b>5. How quickly can private acquisition financing be secured?</u></b><br>
    •Answer: Private lenders can often close acquisition loans within weeks, faster than traditional banks.
</p>

    <p><u><b>6. Is collateral required for a private acquisition loan?</u></b><br>
    •Answer: Yes, loans are typically secured by the acquired company's assets, cash flows, or equity.
</p>

    <p><u><b>7. What are the typical interest rates for private acquisition loans?</u></b><br>
    •Answer: Interest rates are generally higher than bank loans, reflecting increased risk and flexibility.
</p>

    <p><u><b>8. Do private lenders require equity participation?</u></b><br>
    •Answer: Some private lenders may require equity kickers, warrants, or profit participation in addition to interest.
</p>

    <p><u><b>9. What are the repayment terms of an acquisition loan?</u></b><br>
    •Answer: Repayment terms may include amortization, interest-only periods, or bullet payments at maturity.
</p>

    <p><u><b>10. Can acquisition loans be used alongside equity financing?</u></b><br>
    •Answer: Yes, private acquisition loans are often combined with private equity or sponsor capital.
</p>

    <p><u><b>11. What are the benefits of private debt for acquisitions?</u></b><br>
    •Answer: Benefits include speed, flexible terms, higher leverage, and customized deal structures.
</p>

    <p><u><b>12. What are the risks of using private debt for acquisitions?</u></b><br>
    •Answer: Risks include higher interest costs, covenant restrictions, and refinancing pressure.
</p>

    <p><u><b>13. Do private acquisition loans include financial covenants?</u></b><br>
    •Answer: Yes, lenders often impose covenants related to leverage, cash flow, or performance.
</p>

    <p><u><b>14. How does private acquisition debt differ from bank acquisition loans?</u></b><br>
    •Answer: Private debt offers faster execution and flexibility, while bank loans usually offer lower costs but stricter requirements.
</p>

    <p><u><b>15. When should a company consider a private acquisition loan?</u></b><br>
    •Answer: A company should consider private acquisition debt when speed, flexibility, or complex deal structures are required.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtacquisitionloantwelve(request):
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
    Capital Type: Acquisition Loan</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Private acquisition loans are best suited for established, operating companies seeking to acquire another business, business unit, or significant assets. Borrowers are typically growth-stage to mature companies with stable cash flows.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Acquisition loans are commonly structured for C-Corps, LLCs, and S-Corps. Lenders prefer entities with clear ownership structures and the ability to provide guarantees or collateral at the operating company or holding company level.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Borrowers are expected to demonstrate strong historical financial performance, acquisition rationale, and the ability to service debt post-acquisition. Existing debt is acceptable but leverage ratios are closely evaluated.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Private acquisition loans operate in the private credit market, typically provided by private lenders, private credit funds, family offices, and specialty finance firms.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Loan sizes vary widely, commonly ranging from $1 million to $100+ million, depending on deal size, target company cash flow, and collateral coverage.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Acquisition loans are transaction-specific debt facilities, not equity rounds. They are often combined with equity contributions or seller financing to complete the acquisition.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are usually disbursed in a single tranche at closing, though some structures may include holdbacks or earnout-related disbursements.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Permitted uses include:
<br>•   Purchase of business equity or assets
<br>•   Transaction and advisory fees
<br>•   Integration and initial operating costs
Use is restricted strictly to acquisition-related purposes.

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is moderate to high, driven by integration risk, performance of the acquired business, and economic conditions. Lenders mitigate risk through collateral, covenants, and guarantees.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Cost of capital is higher than traditional bank acquisition loans but lower than equity financing. Pricing reflects transaction complexity, leverage, and perceived integration risk.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are moderate to high, including due diligence, legal fees, lender fees, valuation costs, and closing expenses.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is moderate, typically 45–90 days, depending on due diligence, deal structure, and regulatory approvals.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
