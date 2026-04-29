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

def privateequitysecuritiesregulationd506b(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation D 506(b) </center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation D Rule 506(b) offerings are ideal for private companies seeking to raise capital from a select group of investors without registering securities with the SEC. They are designed so that issuers can raise an unlimited amount of capital through private placements, provided sales are limited to accredited investors and up to 35 sophisticated non-accredited investors, with no general solicitation or advertising. {n} fits that definition. In 2026, Rule 506(b) remains one of the most commonly used exemptions for private equity, venture capital, and real asset funds due to its regulatory certainty and federal preemption of state securities registration requirements. It is frequently used by startups, private equity funds, real estate syndications, and holding companies seeking flexible capital formation while maintaining confidentiality. While 506(b) offerings reduce regulatory burden and preserve privacy, they introduce compliance, disclosure, and verification risk. Issuers must carefully manage investor qualification, information parity, and resale restrictions to avoid violations that could jeopardize the exemption and trigger enforcement actions.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Regulation D Rule 506(b) is a safe-harbor exemption under the U.S. Securities Act of 1933 that permits issuers to sell unregistered securities through private offerings without limitation on capital raised, provided that no general solicitation is used. (U.S. Securities and Exchange Commission, 2025)<br><br>
    2. Securities issued under Rule 506(b) are restricted securities, meaning they cannot be freely resold and must comply with holding periods and transfer limitations under Rule 144. These securities sit within the Private Equity segment of the capital markets rather than public equity markets. (SEC, 2025)<br><br>
    3. Legally, Rule 506(b) offerings are governed by offering documents such as a Private Placement Memorandum (PPM), subscription agreements, and investor questionnaires that ensure adequate disclosure and investor suitability, particularly when non-accredited investors participate. (Practising Law Institute, 2025)<br><br>
    4. From a risk perspective, Rule 506(b) offerings expose issuers to regulatory and rescission risk if disclosure is incomplete, misleading, or inconsistent across investors. Investors face liquidity risk due to resale restrictions and limited secondary markets. (Harvard Law School Forum, 2025)<br><br>
    5. From an accounting and process standpoint, capital raised under Rule 506(b) is recorded as Equity or Equity-Linked Securities, depending on structure. The fundraising process is relationship-driven and slower than public offerings but offers greater control over investor selection and terms. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2025). Regulation D Offerings. https://www.sec.gov/smallbusiness/exemptofferings/regulationd<br>
    Practising Law Institute (PLI). (2025). Private Placements under Rule 506(b). https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2025). Private Offerings and Disclosure Risk. https://corpgov.law.harvard.edu<br>
    Deloitte. (2025). Accounting for Equity Issuances and Private Placements. https://www2.deloitte.com/equity-accounting<br>
    CFA Institute. (2025). Private Equity Market Structures. https://www.cfainstitute.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Issuer Eligibility – Private company or investment vehicle<br>
    • Investor Limits – Unlimited accredited investors; up to 35 non-accredited but sophisticated investors<br>
    • No General Solicitation – Prohibition on public advertising or marketing<br>
    • Disclosure Obligations – Enhanced disclosures if non-accredited investors participate<br>
    • Investor Suitability – Sophistication and risk-bearing capacity<br>
    • Resale Restrictions – Rule 144 transfer limitations<br>
    • Form D Filing – SEC notice filing within required timeframe<br>
    • State Blue Sky Compliance – Notice filings and fees (preempted registration)
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Private Placement Memorandum (PPM) – Offering terms and risk disclosures<br>
    • Subscription Agreement – Investor commitment and representations<br>
    • Investor Questionnaire – Accreditation and suitability verification<br>
    • Operating / Shareholder Agreement – Governance and rights<br>
    • Capitalization Table – Ownership before and after issuance<br>
    • Form D Filing – SEC exemption notice<br>
    • Board & Shareholder Resolutions – Authorization to issue securities<br>
    • Legal Opinions – Compliance and enforceability confirmation
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506bfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Regulation D 506(b)</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is Regulation D Rule 506(b)?</u></b><br>
    • Answer: Regulation D Rule 506(b) is a U.S. Securities and Exchange Commission (SEC) exemption that allows companies to raise unlimited capital through private offerings without registering the securities.
    </p>
    <p><u><b>2. Who can invest under Rule 506(b)?</u></b><br>
    • Answer: Investments may be made by an unlimited number of accredited investors and up to 35 non-accredited but sophisticated investors.
    </p>
    <p><u><b>3. What does "sophisticated investor" mean under 506(b)?</u></b><br>
    • Answer: A sophisticated investor is someone with sufficient financial knowledge and experience to evaluate the risks and merits of the investment.
    </p>
    <p><u><b>4. Is general solicitation allowed under Rule 506(b)?</u></b><br>
    • Answer: No, general solicitation or public advertising is not permitted under Rule 506(b).
    </p>
    <p><u><b>5. How much capital can be raised under Rule 506(b)?</u></b><br>
    • Answer: There is no limit on the amount of capital that can be raised under Rule 506(b).
    </p>
    <p><u><b>6. What disclosures are required for 506(b) offerings?</u></b><br>
    • Answer: Issuers must provide specific disclosures to non-accredited investors, similar to those required in registered offerings.
    </p>
    <p><u><b>7. Is SEC registration required for Rule 506(b)?</u></b><br>
    • Answer: No, securities offered under Rule 506(b) are exempt from SEC registration, though a Form D filing is required.
    </p>
    <p><u><b>8. What is Form D in a 506(b) offering?</u></b><br>
    • Answer: Form D is a notice filing submitted to the SEC after securities are sold, providing basic information about the offering.
    </p>
    <p><u><b>9. Are securities sold under Rule 506(b) restricted?</u></b><br>
    • Answer: Yes, securities are restricted and cannot be freely resold without registration or another exemption.
    </p>
    <p><u><b>10. Are state securities laws applicable to 506(b) offerings?</u></b><br>
    • Answer: State registration is preempted, but issuers must comply with state notice filings and fees.
    </p>
    <p><u><b>11. Can companies advertise to existing investors under 506(b)?</u></b><br>
    • Answer: Communications must be limited to pre-existing, substantive relationships and cannot constitute general solicitation.
    </p>
    <p><u><b>12. What types of companies use Rule 506(b)?</u></b><br>
    • Answer: Startups, private equity funds, real estate funds, and private operating companies commonly use Rule 506(b).
    </p>
    <p><u><b>13. What are the benefits of Rule 506(b)?</u></b><br>
    • Answer: Benefits include access to non-accredited investors, no cap on fundraising amount, and reduced regulatory burden.
    </p>
    <p><u><b>14. What are the risks of Rule 506(b) offerings?</u></b><br>
    • Answer: Risks include limited liquidity, reduced disclosure compared to public offerings, and higher investment risk.
    </p>
    <p><u><b>15. When should a company use Regulation D Rule 506(b)?</u></b><br>
    • Answer: A company should use Rule 506(b) when raising private capital from known investors without public marketing.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506btwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Equity Securities</b></u><br>
    Capital Type: Regulation D 506(b)</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Regulation D 506(b) offerings are best suited for early-stage through growth-stage companies that are raising private equity capital without engaging in public solicitation. This exemption is commonly used by startups, private companies, and operating businesses that have a defined business model and are seeking capital from known investors rather than the broader public. {stage} aligns with Rule 506(b) use.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    C-Corporations are the most common entity type for Regulation D 506(b) offerings, particularly for venture-backed companies, as this structure supports equity issuance and investor rights. LLCs may also use 506(b) offerings, especially for real estate or operating businesses. Sole proprietorships are generally not suitable due to ownership and securities compliance constraints. {{entity}} is {{entity}} appropriate.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Companies using Regulation D 506(b) often have raised limited or moderate prior capital through founder funding, friends-and-family rounds, or prior private placements. Excessive prior dilution may complicate valuation and investor terms, but prior fundraising is not a barrier as long as the offering is properly structured. {{preraise}} reflects {{preraise}} prior capital patterns.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    Regulation D 506(b) offerings operate within the private capital markets and are commonly used by angel investors, family offices, and private investment groups. Unlike 506(c), these offerings prohibit general solicitation and rely on pre-existing relationships with investors. {{premarket}} reflects {{premarket}} market positioning.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    There is no statutory limit on the amount of capital that can be raised under Regulation D 506(b). In practice, raises typically range from several hundred thousand dollars to tens of millions of dollars, depending on company stage, investor network, and growth strategy. {{raisegoal}} aligns with 506(b) parameters.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    A 506(b) offering is often structured as a seed, Series A, or growth equity round. It allows companies to include an unlimited number of accredited investors and up to 35 non-accredited but sophisticated investors, provided disclosure requirements are met. {{tranch}} represents {{tranch}} structure.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Funds may be raised in a single close or through multiple rolling closes as investors commit capital over time. Rolling closes are common when leveraging an existing investor network without public marketing. {{rounds}} reflects {{rounds}} approach.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Proceeds from a Regulation D 506(b) offering are typically used for product development, market expansion, hiring, working capital, acquisitions, or general corporate purposes. Use of funds is generally flexible but must align with disclosures made to investors. {{useoffund}} represents {{useoffund}} typical uses.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Investors face high risk due to the illiquid nature of private equity, company execution risk, and lack of public market pricing. For issuers, risk includes compliance risk, disclosure obligations, and limitations on marketing and investor outreach.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    The cost of capital is reflected in equity dilution, investor rights, and potential governance concessions. While there is no interest expense, founders may incur long-term dilution and control considerations. {{enterprisecost}} reflects {{enterprisecost}} cost profile.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs are moderate and include legal structuring, private placement memorandum preparation if required, securities filings, and administrative expenses. Costs increase when non-accredited investors are included due to enhanced disclosure requirements. {{upfrontcost}} is {{upfrontcost}} typical.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing to capital depends on investor relationships and legal preparation but is generally faster than public offerings. Most 506(b) raises are completed within one to three months, depending on deal size and investor engagement. {{upfronttime}} reflects {{upfronttime}} expected timeline.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)