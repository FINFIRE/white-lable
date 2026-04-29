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

def privateequitysecuritiesregulationd504(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation D 504 </center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation D Rule 504 offerings are ideal for early-stage companies and small issuers seeking to raise limited amounts of capital with reduced federal regulatory burden. They are designed so that issuers may offer and sell securities without SEC registration, subject to aggregate offering caps and compliance with applicable state securities laws. {n} fits that definition. In 2026, Rule 504 is primarily used by startups, small businesses, and real estate ventures conducting localized or state-registered offerings. Unlike Rule 506 offerings, Rule 504 does not preempt state securities laws, making it most suitable for issuers willing to comply with state-level registration or exemption frameworks. While Rule 504 provides flexibility and access to non-accredited investors, it introduces state compliance, disclosure, and resale restriction risk. Issuers must carefully manage offering structure and jurisdictional requirements to maintain exemption eligibility.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Regulation D Rule 504 is a federal securities exemption under the U.S. Securities Act of 1933 that allows eligible issuers to raise a limited amount of capital through unregistered offerings, subject to aggregate offering limits. (U.S. Securities and Exchange Commission, 2025)<br><br>
    2. Securities issued under Rule 504 are generally considered restricted securities, unless sold under a state registration or exemption that permits public resale. These offerings fall within the Private Equity Securities segment rather than public capital markets. (SEC, 2025)<br><br>
    3. Legally, Rule 504 offerings are governed by offering documents such as a Private Placement Memorandum (PPM), subscription agreements, and state-level filings. Unlike Rule 506, federal preemption does not apply, requiring compliance with applicable state securities laws. (Practising Law Institute, 2025)<br><br>
    4. From a risk perspective, Rule 504 offerings expose issuers to multi-jurisdictional compliance risk, including inconsistent state disclosure standards and potential rescission liability. Investors face liquidity risk due to resale restrictions and limited secondary markets. (Harvard Law School Forum, 2025)<br><br>
    5. From an accounting and process standpoint, capital raised under Rule 504 is recorded as Equity or Equity-Linked Securities, depending on instrument structure. Fundraising timelines may be longer than Rule 506 offerings due to state review and registration requirements. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2025). Regulation D: Rule 504 Offerings. https://www.sec.gov/smallbusiness/exemptofferings<br>
    Practising Law Institute (PLI). (2025). State Blue Sky Compliance for Rule 504. https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2025). Private Offering Exemptions and State Law. https://corpgov.law.harvard.edu<br>
    Deloitte. (2025). Accounting for Private Equity Issuances. https://www2.deloitte.com/equity<br>
    CFA Institute. (2025). Private Capital Formation Structures. https://www.cfainstitute.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Issuer Eligibility – Non-reporting private company<br>
    • Capital Raise Limit – Aggregate offering cap per 12-month period<br>
    • Investor Eligibility – Accredited and non-accredited investors permitted<br>
    • State Securities Compliance – Registration or exemption required<br>
    • Disclosure Obligations – State-mandated investor disclosures<br>
    • Resale Restrictions – Restricted or state-permitted securities<br>
    • Form D Filing – SEC notice filing<br>
    • Anti-Fraud Compliance – Full and fair disclosure requirements
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Private Placement Memorandum (PPM) – Offering disclosures<br>
    • Subscription Agreement – Investor commitments<br>
    • Investor Questionnaire – Suitability information<br>
    • Capitalization Table – Ownership structure<br>
    • Form D Filing – SEC exemption notice<br>
    • State Blue Sky Filings – Registration or exemption documents<br>
    • Board & Shareholder Resolutions – Authorization to issue securities<br>
    • Legal Opinions – Compliance and exemption confirmation
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd504faq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities – Regulation D Rule 504<br>
    Private Equity</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is Regulation D Rule 504?</u></b><br>
    • Answer: Regulation D Rule 504 is a U.S. SEC exemption that allows companies to raise limited capital through private offerings without full SEC registration.
    </p>
    <p><u><b>2. How much capital can be raised under Rule 504?</u></b><br>
    • Answer: Issuers can raise up to $10 million in any 12-month period under Rule 504.
    </p>
    <p><u><b>3. Who can invest under Rule 504?</u></b><br>
    • Answer: Both accredited and non-accredited investors may invest, subject to state securities laws.
    </p>
    <p><u><b>4. Is general solicitation allowed under Rule 504?</u></b><br>
    • Answer: General solicitation is generally prohibited unless the offering meets specific state law registration or exemption requirements.
    </p>
    <p><u><b>5. Are disclosure requirements mandatory under Rule 504?</u></b><br>
    • Answer: Disclosure requirements are governed primarily by state securities ("blue sky") laws rather than federal rules.
    </p>
    <p><u><b>6. Is SEC registration required for Rule 504 offerings?</u></b><br>
    • Answer: No SEC registration is required, but issuers must file Form D with the SEC.
    </p>
    <p><u><b>7. Are securities issued under Rule 504 restricted?</u></b><br>
    • Answer: Securities may be restricted unless the offering is registered at the state level or qualifies for certain exemptions.
    </p>
    <p><u><b>8. Do state securities laws apply to Rule 504 offerings?</u></b><br>
    • Answer: Yes, issuers must comply with applicable state securities laws and regulations.
    </p>
    <p><u><b>9. What types of companies use Rule 504?</u></b><br>
    • Answer: Early-stage companies, small businesses, and startups commonly use Rule 504.
    </p>
    <p><u><b>10. How does Rule 504 differ from Rule 506(b)?</u></b><br>
    • Answer: Rule 504 has a fundraising cap and is subject to state regulation, while Rule 506(b) allows unlimited capital with federal preemption.
    </p>
    <p><u><b>11. Can non-accredited investors freely resell Rule 504 securities?</u></b><br>
    • Answer: Resale depends on state registration or exemption status and whether securities are deemed unrestricted.
    </p>
    <p><u><b>12. What are the benefits of Rule 504?</u></b><br>
    • Answer: Benefits include access to non-accredited investors and simplified federal compliance.
    </p>
    <p><u><b>13. What are the risks of Rule 504 offerings?</u></b><br>
    • Answer: Risks include limited liquidity, state-level compliance complexity, and higher investor risk.
    </p>
    <p><u><b>14. What replaced Rule 504 in larger offerings?</u></b><br>
    • Answer: Larger offerings typically use Regulation D Rule 506(b) or 506(c).
    </p>
    <p><u><b>15. When should a company use Rule 504?</u></b><br>
    • Answer: A company should use Rule 504 when raising smaller amounts of capital and targeting local or regional investors.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd504twelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Equity Securities – Regulation D 504</b></u><br>
    Capital Type: Private Placement Equity (Exempt Offering)</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Regulation D 504 offerings are best suited for early-stage through growth-stage companies seeking to raise smaller amounts of private equity capital without engaging in public markets. This exemption is commonly used by startups, small businesses, and operating companies that are building initial traction or expanding operations. {stage} aligns with Rule 504 use cases.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    C-Corporations and LLCs are commonly used entity types for Regulation D 504 offerings, as both structures support equity issuance and private investment. Sole proprietorships are generally not suitable due to securities law and ownership limitations. {{entity}} is {{entity}} appropriate for Rule 504 offerings.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Companies using Regulation D 504 often have limited to moderate prior capital, including founder investment, friends-and-family funding, or early angel capital. The exemption is well-suited for issuers that are early in their fundraising lifecycle and have relatively simple capital structures. {{n}}'s prior capital of {{preraise}} is {{preraise}} typical for Rule 504 issuers.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    Regulation D 504 operates within the private capital markets and is typically used by angel investors, local investment groups, and small private funds. Certain state-level rules may permit broader solicitation when paired with state registration or qualification. {{n}}'s pre-market positioning of {{premarket}} reflects {{premarket}} prior market activity.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    Regulation D 504 allows issuers to raise up to $10 million within a 12-month period, subject to compliance with federal and applicable state securities laws. This cap makes the exemption appropriate for smaller raises rather than large institutional rounds. {{n}}'s target of {{raisegoal}} aligns with Rule 504 parameters.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    A 504 offering is commonly structured as a seed or early growth equity round. The exemption permits sales to accredited and non-accredited investors, provided offering requirements and disclosures are properly met. {{tranch}} represents {{tranch}} appropriate structure.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Funds may be raised in a single close or through multiple rolling closes over the offering period, allowing issuers to accept capital incrementally while remaining within the annual raise limit. {{rounds}} reflects {{rounds}} tranching approach.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Proceeds are typically used for product development, early operations, hiring, marketing, expansion, or general corporate purposes. Use of funds must align with disclosures made to investors. {{useoffund}} represents {{useoffund}} typical deployment.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Investor risk is high due to early-stage business risk, limited liquidity, and reduced disclosure compared to public offerings. Issuers face compliance risk, particularly with respect to state securities laws and investor communications.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    The cost of capital is primarily equity dilution and potential investor rights rather than interest expense. Founders may also incur governance or information rights concessions as part of the offering. {{enterprisecost}} reflects {{enterprisecost}} cost profile.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs are low to moderate and include legal structuring, securities filings, offering documentation, and administrative expenses. Costs may increase if state registration or qualification is required. {{upfrontcost}} is {{upfrontcost}} typical for Rule 504.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing to capital is generally efficient compared to registered offerings and often ranges from a few weeks to two months, depending on legal preparation, state compliance, and investor participation. {{upfronttime}} represents {{upfronttime}} expected timeline.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)