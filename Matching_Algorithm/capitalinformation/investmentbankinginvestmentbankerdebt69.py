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

def investmentbankinginvestmentbankerdebt(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Investment Banking</b></u><br>
    Capital Type: Investment Banker Debt </center></p>
    <p><b><u>Introduction</u></b><br>
    Investment Banker Debt is ideal for companies seeking structured debt capital arranged, underwritten, or distributed by investment banks to support acquisitions, refinancings, growth initiatives, or capital structure optimization. It is designed so that debt instruments are engineered and placed through investment banking channels, often combining market access, bespoke structuring, and institutional distribution. {n} fits that definition. In 2026, investment banker–arranged debt remains central to capital markets activity, spanning syndicated loans, bridge loans, high-yield bonds, structured notes, and private placements. Investment banks play a critical role in underwriting risk, coordinating lenders or investors, and tailoring debt solutions to issuer credit profiles and market conditions. While investment banker debt provides scale and market access, it introduces market execution, underwriting, and refinancing risk. Issuers are exposed to pricing volatility, covenant complexity, and dependency on capital market conditions at issuance and rollover.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Investment Banker Debt refers to debt financing arranged, underwritten, or syndicated by investment banks on behalf of issuers, including corporate, sponsor-backed, or sovereign entities. Instruments may be public or private and span loans, bonds, or hybrid structures. (Corporate Finance Institute, 2026)<br><br>
    2. Investment banker debt occupies a defined position within the Capital Stack, typically as senior secured, senior unsecured, or subordinated debt depending on structure. Ranking and recovery depend on contractual terms and intercreditor arrangements. (Moody's Investors Service, 2025)<br><br>
    3. Legally, investment banker debt is governed by Underwriting Agreements, Credit Agreements, or Indentures, which define pricing, allocation, covenants, and distribution mechanics. Investment banks may assume underwriting risk or act solely as placement agents. (Latham & Watkins, 2025)<br><br>
    4. From a risk perspective, investment banker debt exposes issuers to market timing, syndication, and refinancing risk, while investors face credit and liquidity risk tied to issuer performance and market conditions. Failed syndications or adverse market moves can alter deal economics. (S&P Global Ratings, 2025)<br><br>
    5. From an accounting and process standpoint, investment banker debt is recorded as Long-Term or Short-Term Liabilities by issuers, with underwriting fees capitalized or expensed according to accounting standards. The issuance process is market-driven and subject to investor demand and pricing dynamics. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Corporate Finance Institute (CFI). (2026). Debt Capital Markets and Investment Banking. https://corporatefinanceinstitute.com/resources/credit-analysis<br>
    Moody's Investors Service. (2025). Debt Structures and Recovery Analysis. https://www.moodys.com<br>
    Latham & Watkins. (2025). Debt Capital Markets Legal Framework. https://www.lw.com/debt-capital-markets<br>
    S&P Global Ratings. (2025). Credit Risk in Capital Markets Debt. https://www.spglobal.com/ratings<br>
    Deloitte. (2025). Accounting for Debt Issuance Costs. https://www2.deloitte.com/debt-accounting
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Issuer Eligibility – Corporate, sponsor-backed, or sovereign issuer<br>
    • Mandate Agreement – Engagement of investment bank<br>
    • Credit Assessment – Rating or investor credit review<br>
    • Disclosure Documentation – Offering memorandum or prospectus<br>
    • Regulatory Compliance – Securities and lending regulations<br>
    • Syndication or Distribution Terms – Investor allocation rules<br>
    • Covenants & Security – Structural protections<br>
    • Board & Shareholder Approvals – Authorization to incur debt
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • Engagement / Mandate Letter – Investment bank appointment<br>
    • Term Sheet – Commercial and structural terms<br>
    • Underwriting or Placement Agreement – Distribution mechanics<br>
    • Credit Agreement or Indenture – Debt instrument terms<br>
    • Offering Memorandum / Prospectus – Investor disclosures<br>
    • Financial Model – Cash flow and leverage analysis<br>
    • Rating Agency Reports – Credit assessments<br>
    • Board Resolutions – Transaction approvals
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankinginvestmentbankerdebtfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Investment Banking <br>
    Investment Banker Debt</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is investment banker debt?</u></b><br>
    • Answer: Investment banker debt refers to debt financing arranged, structured, or underwritten by investment banks for corporations or institutions.
    </p>
    <p><u><b>2. Who provides investment banker debt?</u></b><br>
    • Answer: The debt is sourced from capital markets investors, institutional lenders, or syndicates, with investment banks acting as arrangers or underwriters.
    </p>
    <p><u><b>3. When is investment banker debt typically used?</u></b><br>
    • Answer: It is used for large-scale financing needs such as acquisitions, refinancings, expansions, or capital structure optimization.
    </p>
    <p><u><b>4. How does investment banker debt work?</u></b><br>
    • Answer: Investment banks structure the debt, price the risk, market it to investors, and facilitate issuance and settlement.
    </p>
    <p><u><b>5. What types of debt fall under investment banker debt?</u></b><br>
    • Answer: It can include corporate bonds, syndicated loans, mezzanine debt, bridge loans, and structured credit products.
    </p>
    <p><u><b>6. Is investment banker debt secured or unsecured?</u></b><br>
    • Answer: It may be secured or unsecured, depending on the issuer's credit profile and transaction structure.
    </p>
    <p><u><b>7. How are interest rates determined for investment banker debt?</u></b><br>
    • Answer: Rates are determined by market conditions, issuer credit rating, maturity, structure, and investor demand.
    </p>
    <p><u><b>8. What is the typical tenure of investment banker debt?</u></b><br>
    • Answer: Tenure varies widely, from short-term bridge financing to long-term bonds of 10 years or more.
    </p>
    <p><u><b>9. What role do investment banks play in the debt process?</u></b><br>
    • Answer: They advise on structure, underwrite or place the debt, manage investor relations, and handle regulatory requirements.
    </p>
    <p><u><b>10. What are the benefits of investment banker debt for issuers?</u></b><br>
    • Answer: Benefits include access to large pools of capital, customized structures, and efficient execution.
    </p>
    <p><u><b>11. What are the risks associated with investment banker debt?</u></b><br>
    • Answer: Risks include market volatility, refinancing risk, covenant restrictions, and higher issuance costs.
    </p>
    <p><u><b>12. How does investment banker debt differ from bank loans?</u></b><br>
    • Answer: Investment banker debt is market-based and scalable, while bank loans are relationship-driven and balance-sheet based.
    </p>
    <p><u><b>13. Who typically uses investment banker debt?</u></b><br>
    • Answer: Large corporations, financial institutions, infrastructure companies, and governments commonly use it.
    </p>
    <p><u><b>14. Are covenants common in investment banker debt?</u></b><br>
    • Answer: Yes, covenants often include financial ratios, reporting requirements, and restrictions on additional debt.
    </p>
    <p><u><b>15. When should a company consider investment banker debt?</u></b><br>
    • Answer: A company should consider it when it needs sizable, structured financing and access to capital markets.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankinginvestmentbankerdebttwelve(request):
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
    Capital Type: Investment Banker Debt</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Investment banker–arranged debt is best suited for late-stage or mature companies with established revenue, strong operating history, and the scale required to access institutional capital markets. This form of financing is generally not appropriate for early-stage startups, as it requires predictable cash flows and robust financial reporting.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    C-Corporations are the primary entity type for investment banker–arranged debt due to regulatory, disclosure, and market requirements. Large LLCs or holding companies may also qualify in certain structures, but sole proprietorships are not suitable.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Companies pursuing investment banker debt typically have significant prior capitalization, including equity investment and existing debt facilities. Underwriting focuses on leverage ratios, cash flow coverage, credit profile, and refinancing or growth strategy rather than early-stage fundraising history.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Investment banker–arranged debt operates within the institutional debt capital markets. Investment banks act as arrangers or underwriters, placing debt with institutional investors such as insurance companies, pension funds, asset managers, and private credit funds.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Debt amounts arranged by investment banks typically range from tens of millions to several billion dollars, depending on issuer size, credit quality, and transaction objectives. Capital size is driven by balance sheet capacity and strategic funding needs.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Investment banker debt is not considered a capital round and does not involve equity issuance. It is structured as term loans, notes, or bond issuances with defined maturities and repayment schedules.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Debt facilities may be issued as a single tranche or multiple tranches with varying maturities, seniority, or pricing. Multi-tranche structures are common to optimize investor demand and cost of capital.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Proceeds are typically used for refinancing existing debt, funding acquisitions, supporting capital expenditures, recapitalizations, or general corporate purposes. Use of funds is generally flexible but governed by debt covenants.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk to investors includes credit risk, interest rate risk, and issuer performance risk. For issuers, risk includes increased leverage, covenant restrictions, refinancing risk, and exposure to market conditions.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    The cost of capital depends on market conditions, credit rating, and structure and includes interest payments, underwriting spreads, and fees. While generally lower than high-yield or mezzanine debt, costs are higher than traditional bank loans for comparable credit risk.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are significant and include investment banking fees, legal and disclosure documentation, due diligence expenses, and ratings agency fees when applicable. These costs are justified by the scale and complexity of the financing.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing to capital typically ranges from two to four months, depending on transaction complexity, market conditions, and regulatory requirements.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
