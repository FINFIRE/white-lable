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


@login_required
def venturecapitalmezzaninefinancing(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name


    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Venture Capital</b></u><br>
    Capital Type: Mezzanine Financing</center></p>
    <p><b><u>Introduction</u></b><br>
    Mezzanine financing is a hybrid form of capital that combines elements of debt and equity, typically used by growth-stage companies to finance expansion, acquisitions, or recapitalizations. {n} fits that definition. It is positioned between senior debt and equity in a company’s capital structure and often includes subordinated debt with equity features such as warrants or conversion rights. Venture capital and private equity investors frequently use mezzanine financing to enhance returns while providing companies with flexible capital solutions. In the United States, mezzanine securities offerings are regulated under the Securities Act of 1933 and overseen by the U.S. Securities and Exchange Commission when structured as securities offerings.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Mezzanine financing is a subordinated form of debt that may include equity participation rights. It ranks below senior secured loans but above common equity in the event of liquidation. Typically, mezzanine capital carries higher interest rates than traditional bank loans due to increased risk and may include payment-in-kind (PIK) interest or warrants allowing lenders to acquire equity at a later date. This structure provides investors with enhanced return potential while offering companies capital without immediate ownership dilution.<br>
    <br>
    2.	Mezzanine financing is best suited for established, revenue-generating companies with stable cash flows seeking growth capital, acquisitions, leveraged buyouts (LBOs), or recapitalization. Companies that have maximized senior debt capacity but wish to avoid significant equity dilution often turn to mezzanine funding. It is commonly used in private equity-backed transactions and expansion financing.<br>
    <br>
    3. Mezzanine financing transactions are typically structured as private placements under Regulation D exemptions from registration under the Securities Act of 1933. Investors are generally accredited or institutional investors due to the risk profile and complexity of the instrument. The regulatory framework ensures disclosure requirements and anti-fraud protections while allowing capital formation flexibility in private markets (SEC, 2023).<br>
    <br>
    4. Mezzanine financing carries higher interest rates and may include equity dilution through warrants or conversion features. Because it is subordinated to senior debt, mezzanine lenders face higher repayment risk in default scenarios. For companies, excessive leverage may strain cash flow and increase financial vulnerability during economic downturns. Investors face liquidity risk, as mezzanine investments are typically not publicly traded.<br>
    <br>
    5. To secure mezzanine financing, companies must demonstrate consistent cash flow, strong EBITDA performance, and a clear growth or acquisition strategy. Investors conduct extensive due diligence, reviewing audited financial statements, capital structure, management credibility, and exit strategy. Successful mezzanine transactions depend on stable earnings, well-structured repayment terms, and alignment between investor return expectations and company growth projections.
    </p> 
        </p>
    <p><u><b>References</b></u><br>
    <br>1.	U.S. Securities and Exchange Commission. (2023). Regulation D Offerings.
    <br>https://www.sec.gov/smallbusiness/exemptofferings/regd 
    <br>2.	Securities Act of 1933. (1933). https://www.sec.gov/about/laws/sa33.pdf 
    <br>3.	Investopedia. (n.d.). Mezzanine Financing Definition.
    <br>https://www.investopedia.com/terms/m/mezzaninefinancing.asp
    <br>4.	Harvard Law School Forum on Corporate Governance. (2020). Private Capital Structures and Subordinated Debt. https://corpgov.law.harvard.edu
    <br>5.	Corporate Finance Institute. (n.d.). Mezzanine Financing Overview.
    <br>https://corporatefinanceinstitute.com/resources/commercial-lending/mezzanine-financing/
    </p>                            
    <p><u><b>Legal Qualification Requirements</u></b><br>
    •	Structured under Regulation D or other applicable exemption
    <br>•	Accredited or Institutional Investor Participation
    <br>•	Compliance with the Securities Act of 1933
    <br>•	Disclosure of Material Financial Risks
    <br>•	Subordination Agreement (if applicable)
    <br>•	Corporate Authorization for Debt Issuance
    <br>•	AML/KYC Compliance

    </p>
    <p><u><b>Supporting Document List</u></b><br>
    •	Private Placement Memorandum (PPM)
    <br>•	Subordinated Loan Agreement
    <br>•	Warrant or Conversion Agreement
    <br>•	Intercreditor Agreement
    <br>•	Audited Financial Statements
    <br>•	Capitalization Table
    <br>•	Risk Disclosure Statement
    <br>•	Subscription Agreement
    <br>•	Corporate Resolutions Authorizing Financing
    """)

    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)


@login_required
def venturecapitalmezzaninefinancingfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Venture Capital  <br>
    Mezzanine Financing </center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1.	What is mezzanine financing in venture capital?</u></b><br>
    • Answer: Mezzanine financing is a hybrid form of capital that combines debt and equity features, typically used by growth-stage companies seeking expansion funding.
    </p>
    <p><u><b>2.	How does mezzanine financing work?</u></b><br>
    • Answer: It is usually structured as subordinated debt that may include warrants or conversion rights into equity if certain conditions are met.
    </p>
    <p><u><b>3.	Where does mezzanine financing sit in the capital stack?</u></b><br>
    • Answer: Mezzanine financing ranks below senior debt but above common equity in the capital structure.
    </p>
    <p><u><b>4.	Who provides mezzanine financing?</u></b><br>
    • Answer: Mezzanine capital is typically provided by specialized mezzanine funds, private equity firms, venture capital firms, or institutional investors.
    </p>
    <p><u><b>5.	When is mezzanine financing commonly used?</u></b><br>
    • Answer: It is often used for business expansion, acquisitions, recapitalizations, or preparing for an IPO or major liquidity event.
    </p>
    <p><u><b>6.	Does mezzanine financing require collateral?</u></b><br>
    • Answer: It may have limited collateral and is often unsecured or subordinated, relying more on company cash flow performance.
    </p>
    <p><u><b>7.	What are the interest rates for mezzanine financing?</u></b><br>
    • Answer: Interest rates are generally higher than senior debt due to increased risk and subordinate position.
    </p>
    <p><u><b>8.	Does mezzanine financing cause ownership dilution?</u></b><br>
    • Answer: Yes, dilution may occur if the financing includes warrants or equity conversion features.
    </p>
    <p><u><b>9.	What are the benefits of mezzanine financing?</u></b><br>
    • Answer: Benefits include access to substantial growth capital without immediate full equity dilution and flexible repayment structures.
    </p>
    <p><u><b>10. What are the risks of mezzanine financing?</u></b><br>
    • Answer: Risks include high capital costs, restrictive covenants, and potential loss of equity through conversion rights.
    </p>
    <p><u><b>11.	How is mezzanine financing repaid?</u></b><br>
    • Answer: Repayment may include periodic interest payments with a balloon payment at maturity or conversion into equity.
    </p>
    <p><u><b>12.	How does mezzanine financing differ from venture equity?</u></b><br>
    • Answer: Venture equity involves direct ownership stakes, while mezzanine financing primarily functions as debt with potential equity upside.
    </p>
    <p><u><b>13.	Is mezzanine financing suitable for early-stage startups?</u></b><br>
    • Answer: It is typically more suitable for later-stage or revenue-generating companies with stable cash flow.
    </p>
    <p><u><b>14. Can mezzanine financing be combined with other capital sources?</u></b><br>
    • Answer: Yes, it is often layered between senior debt and equity in leveraged transactions.
    </p>
    <p><u><b>15. When should a company consider mezzanine financing?</u></b><br>
    • Answer: A company should consider mezzanine financing when seeking growth capital while balancing debt leverage and equity dilution.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)


@login_required
def venturecapitalmezzaninefinancingtwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Venture Capital  </b></u><br>
    Capital Type: Mezzanine Financing</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
       Mezzanine financing is best suited for late-stage venture or growth-stage companies that:
    <br>•	Have strong revenue traction
    <br>•	Are approaching profitability or are profitable
    <br>•	Are preparing for IPO, acquisition, or major expansion
    <br>•	Require growth capital without immediate full equity dilution
    <br>It is typically used between senior debt and pure equity financing.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Most appropriate for:
    <br>•	C-Corporations
    <br>•	Scalable venture-backed companies
    <br>•	PE-backed portfolio companies
    <br>•	Mature startups preparing for exit
    <br>Companies must have predictable cash flow to service debt components.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Before securing mezzanine financing, companies typically need:
    <br>•	Solid financial statements
    <br>•	Revenue visibility and growth metrics
    <br>•	Clear exit strategy (IPO or M&A)
    <br>•	Existing equity investors
    <br>•	Defined capital structure
    <br>Mezzanine investors assess downside protection and upside participation.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    Mezzanine financing operates within the private capital markets, often provided by:
    <br>•	Venture capital growth funds
    <br>•	Private equity funds
    <br>•	Specialized mezzanine debt funds
    <br>These investments are structured under private securities exemptions governed by the U.S. Securities and Exchange Commission.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Typical raise sizes range from:
    <br>•	$5 million to $100+ million, depending on company size
    <br>•	Larger growth companies may raise significantly more
    <br>Often structured as part of a larger capital round.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
     Mezzanine financing typically includes:
    <br>•	Subordinated debt
    <br>•	Convertible debt
    <br>•	Preferred equity with warrants
    <br>•	Debt with equity kickers
    <br>It ranks below senior debt but above common equity in liquidation.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funding may occur:
    <br>•	In a single closing
    <br>•	In milestone-based tranches
    <br>•	Alongside senior debt facilities
    <br>Repayment terms are often structured with balloon payments at maturity.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Common uses include:
    <br>•	Expansion into new markets
    <br>•	Acquisitions
    <br>•	Pre-IPO growth funding
    <br>•	Refinancing existing obligations
    <br>•	Working capital scaling
    <br>Often used as “bridge-to-exit” capital.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk level: Moderate to High
    <br>Risks include:
    <br>•	Subordination risk
    <br>•	Cash flow pressure from interest payments
    <br>•	Equity dilution from warrants or conversion
    <br>•	Exit timing dependency
    Investors rely heavily on successful exit outcomes.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Capital costs are generally higher than senior debt and may include:
    <br>•	Interest rates (often 10%–20% effective yield)
    <br>•	Warrants or equity participation
    <br>•	Exit bonuses
    <br>•	Structuring fees
    <br>Total cost can be significant but less dilutive than full equity raises.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are moderate to high, including:
    <br>•	Legal documentation
    <br>•	Due diligence expenses
    <br>•	Financial modeling
    <br>•	Advisory or placement fees
    <br>Negotiation complexity increases documentation costs.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
     Typical timeline: 2–5 months, depending on:
    <br>•	Financial readiness
    <br>•	Investor due diligence
    <br>•	Complexity of capital structure
    <br>Mezzanine can close faster than IPO processes but slower than traditional venture rounds.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
