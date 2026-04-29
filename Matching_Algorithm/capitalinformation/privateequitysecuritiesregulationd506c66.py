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

def privateequitysecuritiesregulationd506c(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Regulation D 506(c) </center></p>
    <p><b><u>Introduction</u></b><br>
    Regulation D Rule 506(c) offerings are ideal for private companies and funds seeking to raise capital through public solicitation while limiting participation exclusively to accredited investors. They are designed so that issuers may broadly market their offerings, including through online platforms and general advertising, provided that all investors are verified as accredited. {n} fits that definition. In 2026, Rule 506(c) has become increasingly popular among startups, real estate sponsors, and private funds leveraging digital distribution and online investor networks. The exemption enables faster capital formation and wider visibility compared to Rule 506(b), while imposing stricter investor verification requirements. While Rule 506(c) expands marketing flexibility, it introduces verification, privacy, and compliance risk. Issuers must take reasonable steps to verify accredited status and maintain records demonstrating compliance to preserve the exemption.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Regulation D Rule 506(c) is a safe-harbor exemption under the U.S. Securities Act of 1933 that permits issuers to engage in general solicitation and advertising, provided that all purchasers in the offering are accredited investors. (U.S. Securities and Exchange Commission, 2025)<br><br>
    2. Securities issued under Rule 506(c) are restricted securities, subject to resale limitations under Rule 144, and are classified within the Private Equity Securities market rather than public equity markets. (SEC, 2025)<br><br>
    3. Legally, Rule 506(c) offerings require issuers to take reasonable steps to verify each investor's accredited status using documentation such as income records, net-worth verification, or third-party certifications. Offering documents typically include a Private Placement Memorandum (PPM) and subscription agreements. (Practising Law Institute, 2025)<br><br>
    4. From a risk perspective, Rule 506(c) offerings expose issuers to verification, recordkeeping, and regulatory enforcement risk. Failure to properly verify investors or maintain documentation can invalidate the exemption and trigger rescission rights. (Harvard Law School Forum, 2025)<br><br>
    5. From an accounting and process standpoint, capital raised under Rule 506(c) is recorded as Equity or Equity-Linked Securities, depending on structure. Fundraising can be faster than Rule 506(b) due to broader marketing, but requires enhanced compliance infrastructure. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2025). Regulation D and Rule 506(c). https://www.sec.gov/smallbusiness/exemptofferings/regulationd<br>
    Practising Law Institute (PLI). (2025). General Solicitation and Accredited Investor Verification. https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2025). Private Offerings and General Solicitation. https://corpgov.law.harvard.edu<br>
    Deloitte. (2025). Accounting for Private Capital Raises. https://www2.deloitte.com/equity<br>
    CFA Institute. (2025). Private Markets and Investor Access. https://www.cfainstitute.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Issuer Eligibility – Private company or fund<br>
    • Investor Eligibility – Accredited investors only<br>
    • General Solicitation Permitted – Public marketing allowed<br>
    • Accredited Verification – Reasonable verification procedures required<br>
    • Disclosure Obligations – Full and fair disclosure of risks and terms<br>
    • Resale Restrictions – Rule 144 transfer limitations<br>
    • Form D Filing – SEC notice filing<br>
    • State Blue Sky Compliance – Notice filings and fees
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Private Placement Memorandum (PPM) – Offering disclosures<br>
    • Subscription Agreement – Investor commitments<br>
    • Accredited Investor Verification Documents – Income or net-worth proof<br>
    • Third-Party Verification Letters – CPA, attorney, or broker confirmations<br>
    • Capitalization Table – Ownership structure<br>
    • Form D Filing – SEC exemption notice<br>
    • Board & Shareholder Resolutions – Authorization to issue securities<br>
    • Legal Opinions – Exemption and compliance confirmation
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506cfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Regulation D 506(c)</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is Regulation D Rule 506(c)?</u></b><br>
    • Answer: Regulation D Rule 506(c) is a U.S. SEC exemption that allows companies to raise unlimited capital through private offerings using general solicitation, provided all investors are accredited.
    </p>
    <p><u><b>2. Who can invest under Rule 506(c)?</u></b><br>
    • Answer: Only accredited investors are permitted to invest under Rule 506(c).
    </p>
    <p><u><b>3. Is general solicitation allowed under Rule 506(c)?</u></b><br>
    • Answer: Yes, issuers are allowed to publicly advertise and solicit investors.
    </p>
    <p><u><b>4. How much capital can be raised under Rule 506(c)?</u></b><br>
    • Answer: There is no limit on the amount of capital that can be raised.
    </p>
    <p><u><b>5. What investor verification is required under Rule 506(c)?</u></b><br>
    • Answer: Issuers must take reasonable steps to verify accredited investor status using documentation or third-party verification.
    </p>
    <p><u><b>6. Is SEC registration required for Rule 506(c)?</u></b><br>
    • Answer: No SEC registration is required, but issuers must file Form D with the SEC.
    </p>
    <p><u><b>7. Are securities issued under Rule 506(c) restricted?</u></b><br>
    • Answer: Yes, securities are restricted and subject to resale limitations.
    </p>
    <p><u><b>8. Are state securities laws applicable to Rule 506(c) offerings?</u></b><br>
    • Answer: State registration is preempted, but notice filings and fees may still apply.
    </p>
    <p><u><b>9. What types of issuers use Rule 506(c)?</u></b><br>
    • Answer: Startups, private equity funds, real estate funds, and private companies commonly use Rule 506(c).
    </p>
    <p><u><b>10. What disclosures are required under Rule 506(c)?</u></b><br>
    • Answer: While specific disclosures are not mandated for accredited investors, anti-fraud rules still apply.
    </p>
    <p><u><b>11. What are the benefits of Rule 506(c)?</u></b><br>
    • Answer: Benefits include unlimited fundraising, public marketing, and streamlined access to accredited investors.
    </p>
    <p><u><b>12. What are the risks of Rule 506(c) offerings?</u></b><br>
    • Answer: Risks include limited liquidity, high investment risk, and compliance failures in investor verification.
    </p>
    <p><u><b>13. How does Rule 506(c) differ from Rule 506(b)?</u></b><br>
    • Answer: Rule 506(c) allows general solicitation but restricts participation to accredited investors only.
    </p>
    <p><u><b>14. Are non-accredited investors allowed under Rule 506(c)?</u></b><br>
    • Answer: No, non-accredited investors are not permitted to invest.
    </p>
    <p><u><b>15. When should a company use Regulation D Rule 506(c)?</u></b><br>
    • Answer: A company should use Rule 506(c) when it wants to publicly market a private offering to accredited investors only.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506ctwelve(request):
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
    Capital Type: Regulation D 506(c)</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Regulation D 506(c) offerings are best suited for early-stage through growth-stage companies that seek to raise private equity capital while publicly marketing their offering. This exemption is commonly used by startups and operating companies that want broader investor reach beyond existing relationships. {stage} aligns with 506(c) use cases.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    C-Corporations are the preferred entity type for Regulation D 506(c) offerings, particularly for venture-backed companies issuing equity securities. LLCs may also utilize 506(c) offerings, especially in operating or real estate contexts. Sole proprietorships are generally not suitable due to securities compliance and ownership limitations. {{entity}} is {{entity}} appropriate.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Companies using Regulation D 506(c) often have limited to moderate prior capital, including founder funding, friends-and-family rounds, or earlier private placements. A clear capitalization structure is important, as investor scrutiny is typically higher due to public solicitation. {{preraise}} reflects {{preraise}} prior capital patterns.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    Regulation D 506(c) operates within the private capital markets and differs from 506(b) by permitting general solicitation and advertising. Capital is sourced exclusively from accredited investors who must be formally verified. {{premarket}} reflects {{premarket}} market positioning.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    There is no statutory limit on the amount of capital that can be raised under Regulation D 506(c). In practice, raises range from several hundred thousand dollars to tens of millions of dollars, depending on company stage, traction, and marketing reach. {{raisegoal}} aligns with 506(c) parameters.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    A 506(c) offering is commonly structured as a seed, Series A, or growth equity round. Unlike 506(b), all investors must be accredited, and issuers are required to take reasonable steps to verify accreditation status. {{tranch}} represents {{tranch}} structure.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Funds may be raised in a single close or through multiple rolling closes as accredited investors commit capital over time. Rolling closes are common due to continuous investor outreach enabled by solicitation. {{rounds}} reflects {{rounds}} approach.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Proceeds are typically used for product development, hiring, market expansion, acquisitions, working capital, or general corporate purposes. Use of funds must align with disclosures made in offering materials. {{useoffund}} represents {{useoffund}} typical uses.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Investor risk remains high due to early-stage execution risk and lack of liquidity. Issuers face increased compliance risk due to verification requirements, public marketing scrutiny, and advertising restrictions under securities laws.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    The cost of capital is primarily equity dilution and investor rights concessions. While no interest is incurred, founders must consider long-term ownership impact and governance implications. {{enterprisecost}} reflects {{enterprisecost}} cost profile.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs are moderate and include legal structuring, offering documentation, accreditation verification services, securities filings, and marketing compliance expenses. Costs are typically higher than 506(b) due to verification requirements. {{upfrontcost}} is {{upfrontcost}} typical.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing to capital depends on marketing effectiveness and investor response but can be relatively fast once solicitation begins. Most 506(c) offerings are completed within one to three months. {{upfronttime}} reflects {{upfronttime}} expected timeline.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
