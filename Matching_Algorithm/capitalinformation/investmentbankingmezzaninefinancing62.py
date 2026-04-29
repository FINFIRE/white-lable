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

def investmentbankingmezzaninefinancing(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Investment Banking</b></u><br>
    Capital Type: Mezzanine Financing </center></p>
    <p><b><u>Introduction</u></b><br>
    Mezzanine Financing is ideal for mature or growth-stage companies seeking flexible capital to fund acquisitions, expansions, recapitalizations, or buyouts without immediate equity dilution or full senior debt constraints. It is designed so that capital is structured as a hybrid of debt and equity, sitting between senior secured debt and common equity in the capital structure. {n} fits that definition. In 2026, mezzanine financing remains a critical tool in leveraged finance and investment banking transactions, particularly in private equity–backed deals and middle-market corporate growth strategies. Investment banks and specialized mezzanine funds structure these instruments to balance yield enhancement for investors with capital efficiency for issuers. While mezzanine financing preserves senior debt capacity and limits upfront dilution, it introduces higher cost, subordination, and refinancing risk. Instruments often include payment-in-kind (PIK) interest, warrants, or conversion features that can materially impact long-term ownership and cash flows.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Mezzanine Financing is a subordinated form of capital that combines features of debt and equity, typically structured as unsecured or second-lien debt with higher interest rates and equity participation through warrants or conversion rights. (Corporate Finance Institute, 2026)<br><br>
    2. Mezzanine financing occupies a defined position within the Capital Stack, ranking below senior secured and unsecured debt but above common equity. In a liquidation scenario, mezzanine investors are repaid after senior lenders and before equity holders. (Moody's Investors Service, 2025)<br><br>
    3. Legally, mezzanine financing is governed by a Mezzanine Credit Agreement and intercreditor arrangements that define payment terms, subordination mechanics, covenants, and enforcement rights relative to senior lenders. (Latham & Watkins, 2025)<br><br>
    4. From a risk perspective, mezzanine financing transfers some downside risk to investors while allowing issuers to optimize leverage. Investors face elevated default and recovery risk, while issuers must manage higher interest burdens and potential equity dilution. (S&P Global Ratings, 2025)<br><br>
    5. From an accounting and process standpoint, mezzanine financing is recorded as Long-Term Debt or Mezzanine Equity depending on structure, with interest expense and potential equity components disclosed separately. Due diligence and structuring complexity make mezzanine transactions more bespoke and slower to execute than senior debt. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Corporate Finance Institute (CFI). (2026). Mezzanine Financing Explained. https://corporatefinanceinstitute.com/resources/credit-analysis<br>
    Moody's Investors Service. (2025). Subordinated Debt and Capital Structures. https://www.moodys.com<br>
    Latham & Watkins. (2025). Mezzanine Finance Structures and Intercreditor Issues. https://www.lw.com/mezzanine-finance<br>
    S&P Global Ratings. (2025). Risk Considerations in Hybrid Capital. https://www.spglobal.com/ratings<br>
    Deloitte. (2025). Accounting for Mezzanine and Hybrid Instruments. https://www2.deloitte.com/mezzanine
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Issuer Eligibility – Growth-stage or mature operating company<br>
    • Defined Use of Proceeds – Acquisition, expansion, or recapitalization<br>
    • Subordination Terms – Ranking relative to senior debt<br>
    • Intercreditor Agreements – Rights and enforcement mechanics<br>
    • Equity Participation Terms – Warrants or conversion features<br>
    • Financial Covenants – Leverage and coverage metrics<br>
    • Regulatory Compliance – Securities and lending regulations<br>
    • Board & Shareholder Approvals – Authorization to issue hybrid capital
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • Mezzanine Credit Agreement – Primary financing contract<br>
    • Term Sheet – Commercial and structural terms<br>
    • Intercreditor Agreement – Priority and subordination mechanics<br>
    • Warrant or Conversion Agreements – Equity participation rights<br>
    • Financial Model – Cash flow and leverage projections<br>
    • Due Diligence Reports – Legal, financial, and tax analysis<br>
    • Board & Shareholder Resolutions – Transaction approvals<br>
    • Legal Opinions – Enforceability and authority confirmations
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankingmezzaninefinancingfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Investment Banking<br>
    Mezzanine Financing</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is mezzanine financing?</u></b><br>
    • Answer: Mezzanine financing is a hybrid form of capital that combines debt and equity features, typically structured as subordinated debt with equity participation.
    </p>
    <p><u><b>2. Who provides mezzanine financing?</u></b><br>
    • Answer: Mezzanine financing is provided by investment banks, private equity firms, mezzanine funds, and institutional investors.
    </p>
    <p><u><b>3. When is mezzanine financing typically used?</u></b><br>
    • Answer: It is commonly used to fund growth, acquisitions, leveraged buyouts, or recapitalizations.
    </p>
    <p><u><b>4. How does mezzanine financing work?</u></b><br>
    • Answer: The lender provides capital that ranks below senior debt but above equity, often with warrants or conversion rights for equity upside.
    </p>
    <p><u><b>5. Is mezzanine financing secured or unsecured?</u></b><br>
    • Answer: Mezzanine financing is usually unsecured or lightly secured and is subordinate to senior debt.
    </p>
    <p><u><b>6. What are the typical returns for mezzanine investors?</u></b><br>
    • Answer: Returns are higher than senior debt and come from interest payments plus equity-linked upside.
    </p>
    <p><u><b>7. What is the typical tenure of mezzanine financing?</u></b><br>
    • Answer: Tenure usually ranges from 5 to 10 years.
    </p>
    <p><u><b>8. What industries commonly use mezzanine financing?</u></b><br>
    • Answer: It is commonly used in middle-market companies across industries such as manufacturing, healthcare, technology, and consumer services.
    </p>
    <p><u><b>9. What are warrants in mezzanine financing?</u></b><br>
    • Answer: Warrants give mezzanine investors the right to purchase equity at a predetermined price, providing upside participation.
    </p>
    <p><u><b>10. How are interest payments structured in mezzanine financing?</u></b><br>
    • Answer: Interest may be cash-pay, payment-in-kind (PIK), or a combination of both.
    </p>
    <p><u><b>11. What are the benefits of mezzanine financing for companies?</u></b><br>
    • Answer: Benefits include flexible capital, limited immediate dilution, and preservation of control.
    </p>
    <p><u><b>12. What are the risks of mezzanine financing?</u></b><br>
    • Answer: Risks include high cost of capital, restrictive covenants, and increased leverage.
    </p>
    <p><u><b>13. How does mezzanine financing differ from senior debt?</u></b><br>
    • Answer: Mezzanine financing is riskier, more expensive, and subordinated compared to senior secured debt.
    </p>
    <p><u><b>14. How does mezzanine financing differ from equity financing?</u></b><br>
    • Answer: It involves less dilution than equity but higher fixed obligations than pure equity.
    </p>
    <p><u><b>15. When should a company consider mezzanine financing?</u></b><br>
    • Answer: A company should consider mezzanine financing when it needs growth capital beyond senior debt capacity and wants to limit equity dilution.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankingmezzaninefinancingtwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Investment Banking</b></u><br>
    Capital Type: Mezzanine Financing</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Mezzanine financing is best suited for late-stage or mature companies with established revenue, positive or near-positive cash flow, and a clear growth or exit strategy. This form of capital is commonly used by companies preparing for expansion, acquisitions, recapitalizations, or private equity transactions and is not appropriate for early-stage startups.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    C-Corporations and LLCs are the most common entity types for mezzanine financing, as these structures can support complex capital stacks and subordinated debt instruments. Sole proprietorships are generally not suitable due to scale, risk profile, and legal complexity.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Companies pursuing mezzanine financing typically have significant prior equity investment and existing senior debt in place. Mezzanine capital is layered between senior debt and equity and relies on the company's ability to service cash interest and provide upside through warrants, options, or conversion features.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Mezzanine financing operates within the private capital markets and is typically arranged through investment banks, private equity firms, mezzanine funds, and institutional investors. This market focuses on structured financing solutions that balance yield and equity upside.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Mezzanine financings commonly range from $5 million to several hundred million dollars, depending on company size, transaction structure, and growth objectives. Capital size is driven by cash flow coverage and overall leverage tolerance.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Mezzanine financing is not a traditional capital round and does not directly involve primary equity issuance. It is structured as subordinated debt with equity-linked features and is often used in conjunction with senior debt and equity in leveraged transactions.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Funds are typically disbursed in a single tranche at closing. In certain transactions, delayed draws or staged funding may be structured to align with acquisition closings or performance milestones.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Mezzanine capital is commonly used for acquisitions, growth expansion, leveraged buyouts, shareholder recapitalizations, or refinancing existing obligations. Use of funds is generally flexible but aligned with transaction objectives and lender covenants.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk to mezzanine investors is higher than senior lenders due to subordination but mitigated by equity participation and contractual protections. For companies, risk includes higher leverage, fixed repayment obligations, and potential equity dilution through warrants or conversion features.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    The cost of mezzanine capital is high relative to senior debt and includes cash interest, payment-in-kind interest, fees, and equity participation. This reflects the higher risk and subordinated position within the capital structure.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are significant and include investment banking fees, legal documentation, financial due diligence, valuation analysis, and structuring expenses. These costs are justified by the complexity and size of mezzanine transactions.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing to capital typically ranges from two to four months, depending on diligence requirements, structuring complexity, and negotiation with investors and lenders.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
