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

def privateequitysecuritiesregulationd505(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation D 505 </center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation D Rule 505 offerings were designed for private companies seeking to raise a limited amount of capital from a mix of accredited and non-accredited investors without registering securities with the SEC. They were structured so that issuers could raise up to a capped amount of capital through private placements while complying with defined investor limits and disclosure requirements. {n} fits that definition. Historically, Rule 505 served as a mid-tier private offering exemption between Rules 504 and 506, commonly used by small businesses and early-stage companies seeking flexibility while maintaining regulatory oversight. Although later superseded by regulatory changes, Rule 505 remains relevant for legacy offerings, historical compliance analysis, and comparative regulatory classification within private equity securities. While Rule 505 reduced registration burden, it introduced disclosure, investor qualification, and resale restriction risk. Issuers were required to carefully manage investor counts, information parity, and state securities compliance to preserve exemption eligibility.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Regulation D Rule 505 was a safe-harbor exemption under the U.S. Securities Act of 1933 that permitted issuers to raise a limited amount of capital through unregistered securities offerings to accredited investors and up to 35 non-accredited investors. (U.S. Securities and Exchange Commission, 2015)<br><br>
    2. Securities issued under Rule 505 were classified as restricted securities, subject to resale limitations and transfer restrictions under federal securities laws. These offerings formed part of the Private Equity Securities market rather than public capital markets. (SEC, 2015)<br><br>
    3. Legally, Rule 505 offerings were governed by offering documents such as a Private Placement Memorandum (PPM), subscription agreements, and investor questionnaires, with enhanced disclosure obligations when non-accredited investors participated. (Practising Law Institute, 2015)<br><br>
    4. From a risk perspective, Rule 505 offerings exposed issuers to regulatory and rescission risk if disclosure standards were not met or investor limits were exceeded. Investors faced liquidity risk due to holding period requirements and limited secondary markets. (Harvard Law School Forum, 2015)<br><br>
    5. From an accounting and process standpoint, capital raised under Rule 505 was recorded as Equity or Equity-Linked Securities, depending on structure. The fundraising process was more constrained than Rule 506 offerings due to capital caps and state securities law applicability. (Deloitte, 2015)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2015). Regulation D Exemptions and Rule 505. https://www.sec.gov/smallbusiness/exemptofferings<br>
    Practising Law Institute (PLI). (2015). Private Offerings under Regulation D. https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2015). Private Placement Exemptions. https://corpgov.law.harvard.edu<br>
    Deloitte. (2015). Accounting for Private Equity Issuances. https://www2.deloitte.com/equity<br>
    CFA Institute. (2015). Private Equity Regulatory Structures. https://www.cfainstitute.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Issuer Eligibility – Private company or investment vehicle<br>
    • Capital Raise Limit – Capped aggregate offering amount<br>
    • Investor Limits – Accredited investors plus up to 35 non-accredited investors<br>
    • Disclosure Obligations – Enhanced disclosures for non-accredited investors<br>
    • Resale Restrictions – Restricted securities subject to transfer limits<br>
    • State Blue Sky Compliance – Registration or qualification required<br>
    • Form D Filing – SEC notice filing<br>
    • Anti-Fraud Compliance – Full and fair disclosure obligations
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Private Placement Memorandum (PPM) – Offering terms and disclosures<br>
    • Subscription Agreement – Investor commitments<br>
    • Investor Questionnaire – Accreditation and suitability confirmation<br>
    • Capitalization Table – Ownership structure<br>
    • Form D Filing – SEC exemption notice<br>
    • State Blue Sky Filings – State-level compliance documents<br>
    • Board & Shareholder Resolutions – Authorization to issue securities<br>
    • Legal Opinions – Exemption and enforceability confirmation
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd505faq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities – Regulation D Rule 505<br>
    Private Equity</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is Regulation D Rule 505?</u></b><br>
    • Answer: Regulation D Rule 505 was a U.S. SEC exemption that allowed companies to raise limited capital through private offerings without full SEC registration.
    </p>
    <p><u><b>2. Is Rule 505 still in effect?</u></b><br>
    • Answer: No, Rule 505 was repealed by the SEC in 2017, but it is still referenced historically in private securities compliance contexts.
    </p>
    <p><u><b>3. How much capital could be raised under Rule 505?</u></b><br>
    • Answer: Issuers could raise up to $5 million in any 12-month period.
    </p>
    <p><u><b>4. Who could invest under Rule 505?</u></b><br>
    • Answer: Offerings could include an unlimited number of accredited investors and up to 35 non-accredited investors.
    </p>
    <p><u><b>5. Was general solicitation allowed under Rule 505?</u></b><br>
    • Answer: No, general solicitation and public advertising were not permitted.
    </p>
    <p><u><b>6. What disclosure requirements applied under Rule 505?</u></b><br>
    • Answer: Issuers were required to provide extensive disclosures to non-accredited investors, similar to registered offerings.
    </p>
    <p><u><b>7. Was SEC registration required under Rule 505?</u></b><br>
    • Answer: No, offerings were exempt from registration, but Form D filing with the SEC was required.
    </p>
    <p><u><b>8. Were securities issued under Rule 505 restricted?</u></b><br>
    • Answer: Yes, securities were restricted and could not be freely resold without registration or an exemption.
    </p>
    <p><u><b>9. Were state securities laws applicable to Rule 505 offerings?</u></b><br>
    • Answer: Yes, issuers were required to comply with applicable state "blue sky" laws.
    </p>
    <p><u><b>10. What types of companies used Rule 505?</u></b><br>
    • Answer: Small and early-stage companies, startups, and private businesses commonly used Rule 505 before its repeal.
    </p>
    <p><u><b>11. How did Rule 505 differ from Rule 506(b)?</u></b><br>
    • Answer: Rule 505 had a fundraising cap and stricter state law requirements, while Rule 506(b) allows unlimited capital and federal preemption.
    </p>
    <p><u><b>12. Why was Rule 505 repealed?</u></b><br>
    • Answer: The SEC repealed it to simplify Regulation D and because Rule 506 made Rule 505 largely unnecessary.
    </p>
    <p><u><b>13. What replaced Rule 505 in practice?</u></b><br>
    • Answer: Most issuers now use Rule 506(b) or Rule 506(c) for private offerings.
    </p>
    <p><u><b>14. What were the benefits of Rule 505?</u></b><br>
    • Answer: Benefits included access to non-accredited investors and reduced federal registration burden.
    </p>
    <p><u><b>15. When is Rule 505 relevant today?</u></b><br>
    • Answer: Rule 505 is relevant primarily for historical reference, legacy compliance review, or analysis of older private offerings.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd505twelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Equity Securities – Regulation D 505</b></u><br>
    Capital Type: Private Placement Equity (Exempt Offering – Repealed / Legacy)</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Regulation D 505 was historically suited for early-stage through growth-stage companies seeking to raise private equity capital under a capped offering size. While this exemption is no longer available for new offerings, it may still be referenced in legacy documentation or historical transactions involving startups and private operating companies. {stage} reflects historical use.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    C-Corporations were the most common entity type for Regulation D 505 offerings, particularly for venture-backed companies issuing equity securities. LLCs were also used in certain operating or real estate contexts. Sole proprietorships were generally not suitable due to securities compliance and ownership limitations. {{entity}} was {{entity}} typical.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Companies relying on Regulation D 505 typically had limited to moderate prior capital, including founder funding, friends-and-family investments, or early angel rounds. The exemption was often used before larger institutional equity rounds occurred. {{preraise}} represents {{preraise}} prior capital patterns.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    Regulation D 505 operated within the private capital markets and was primarily used by angel investors, small private investment groups, and early-stage funds. The market emphasized relationship-driven fundraising rather than broad investor outreach. {{premarket}} reflects {{premarket}} market positioning.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    Regulation D 505 limited issuers to raising up to $5 million within a 12-month period. This cap made the exemption most suitable for smaller early-stage raises rather than large growth financings. {{raisegoal}} aligns with Rule 505 parameters.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    A 505 offering was commonly structured as a seed or early equity round. Issuers were permitted to include up to 35 non-accredited investors along with accredited investors, subject to disclosure requirements. {{tranch}} represents {{tranch}} structure.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Funds were often raised through a single close or multiple rolling closes, allowing issuers to accept investments over time while staying within the aggregate $5 million limit. {{rounds}} reflects {{rounds}} approach.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Proceeds were typically used for product development, early operations, hiring, market entry, and general corporate purposes. Use of funds was flexible but required alignment with investor disclosures. {{useoffund}} represents {{useoffund}} typical uses.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Investor risk was high due to startup execution risk, limited liquidity, and lack of public market transparency. Issuers faced compliance risk related to disclosure obligations and investor suitability requirements.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    The cost of capital was reflected in equity dilution and investor rights rather than interest expense. Issuers often granted preferred terms to compensate investors for early-stage risk. {{enterprisecost}} reflects {{enterprisecost}} cost patterns.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs were moderate and included legal structuring, offering documentation, securities filings, and administrative expenses. Costs increased when non-accredited investors were included due to enhanced disclosure requirements. {{upfrontcost}} is {{upfrontcost}} typical.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing to capital was relatively efficient compared to registered offerings, typically ranging from one to three months depending on legal preparation and investor participation. {{upfronttime}} reflects {{upfronttime}} historical timelines.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)