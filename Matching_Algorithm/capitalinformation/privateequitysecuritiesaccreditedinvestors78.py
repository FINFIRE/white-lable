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

def privateequitysecuritiesaccreditedinvestors(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = """
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Accredited Investors </center></p>
    <p><b><u>Introduction</u></b><br>
    Accredited Investors are ideal participants in private equity securities offerings where issuers seek to raise capital from investors deemed capable of bearing economic risk without the protections of public registration. These offerings are designed so that capital may be raised from individuals or entities meeting specific income, net-worth, or professional qualification thresholds established by securities regulators. {n} fits that definition. In 2026, accredited investors remain the backbone of private capital markets, participating extensively in venture capital, private equity, real estate syndications, hedge funds, and private credit offerings. The accredited investor framework enables efficient capital formation while balancing investor protection through financial sophistication and risk tolerance standards. While reliance on accredited investors simplifies regulatory compliance, it introduces concentration, suitability, and disclosure risk. Issuers must still ensure full and fair disclosure, accurate investor verification, and strict adherence to exemption conditions to preserve offering validity.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. Accredited Investors are individuals or entities that meet defined financial, institutional, or professional criteria under U.S. securities laws, qualifying them to participate in private securities offerings without the protections afforded to retail investors. (U.S. Securities and Exchange Commission, 2025)<br>
    <br>2. Investments made by accredited investors fall squarely within the Private Equity Securities segment of the capital markets and are commonly conducted under exemptions such as Regulation D Rules 506(b) and 506(c), rather than through registered public offerings. (SEC, 2025)<br>
    <br>3. Legally, accredited investor status is determined by income thresholds, net worth standards, or recognized professional certifications, and must be reasonably verified by issuers prior to accepting investment. Documentation requirements vary depending on the exemption relied upon. (Practising Law Institute, 2025)<br>
    <br>4. From a risk perspective, offerings limited to accredited investors reduce regulatory exposure for issuers but do not eliminate anti-fraud, disclosure, or rescission risk. Investors face liquidity constraints, valuation uncertainty, and limited exit options due to resale restrictions. (Harvard Law School Forum, 2025)<br>
    <br>5. From an accounting and process standpoint, capital raised from accredited investors is recorded as Equity or Equity-Linked Securities, depending on the instrument structure. Fundraising is typically relationship-driven and faster than retail offerings due to streamlined suitability requirements. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2025). Accredited Investor Definition and Updates. https://www.sec.gov<br>
    Practising Law Institute (PLI). (2025). Private Placements and Accredited Investors. https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2025). Private Offerings and Investor Protection. https://corpgov.law.harvard.edu<br>
    Deloitte. (2025). Accounting for Private Equity Issuances. https://www2.deloitte.com/equity<br>
    CFA Institute. (2025). Private Capital Markets and Investor Standards. https://www.cfainstitute.org
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Investor Qualification – Income, net worth, or professional certification thresholds<br>
    · Offering Exemption – Regulation D (506(b) or 506(c)) or equivalent<br>
    · Investor Verification – Reasonable steps to confirm accredited status<br>
    · Disclosure Obligations – Full and fair disclosure of risks and terms<br>
    · Resale Restrictions – Restricted securities subject to Rule 144<br>
    · Form D Filing – SEC notice filing requirement<br>
    · State Blue Sky Compliance – Notice filings and fees<br>
    · Anti-Fraud Compliance – Securities law adherence
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Private Placement Memorandum (PPM) – Offering disclosures<br>
    · Subscription Agreement – Investor commitments and representations<br>
    · Accredited Investor Questionnaire – Qualification verification<br>
    · Verification Documents – Income, net worth, or certification evidence<br>
    · Capitalization Table – Ownership structure<br>
    · Form D Filing – SEC exemption notice<br>
    · Board & Shareholder Resolutions – Authorization to issue securities<br>
    · Legal Opinions – Exemption and compliance confirmation
    </p>
    """
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction': introduction,
    }
    return render(request, 'detail.html', context)

def privateequitysecuritiesaccreditedinvestorsfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Accredited Investors</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. Who is considered an accredited investor?</u></b><br>
    •Answer: An accredited investor is an individual or entity that meets income, net worth, or professional criteria defined by securities regulators.
    </p>
    <p><u><b>2. What are the income requirements for accredited investors?</u></b><br>
    •Answer: Individuals must typically have annual income exceeding $200,000 (or $300,000 jointly) for the last two years with an expectation of the same.
    </p>
    <p><u><b>3. What are the net worth requirements for accredited investors?</u></b><br>
    •Answer: Individuals must have a net worth exceeding $1 million, excluding primary residence.
    </p>
    <p><u><b>4. Can entities qualify as accredited investors?</u></b><br>
    •Answer: Yes, entities such as trusts, corporations, funds, and family offices may qualify based on assets or structure.
    </p>
    <p><u><b>5. Are professional certifications relevant for accredited status?</u></b><br>
    •Answer: Yes, certain financial certifications and professional licenses may qualify individuals as accredited investors.
    </p>
    <p><u><b>6. Why are accredited investors important in private equity?</u></b><br>
    •Answer: They are presumed to have financial sophistication and the ability to bear investment risk, enabling access to private offerings.
    </p>
    <p><u><b>7. What types of investments are available to accredited investors?</u></b><br>
    •Answer: Accredited investors can access private equity, venture capital, hedge funds, private placements, and alternative investments.
    </p>
    <p><u><b>8. Are accredited investors protected like retail investors?</u></b><br>
    •Answer: They receive fewer regulatory protections because they are assumed to understand and accept higher risk investments.
    </p>
    <p><u><b>9. How do issuers verify accredited investor status?</u></b><br>
    •Answer: Verification is done through self-certification, documentation, or third-party verification, depending on the offering.
    </p>
    <p><u><b>10. Are investments by accredited investors restricted?</u></b><br>
    •Answer: Yes, private equity securities are typically restricted and subject to resale limitations.
    </p>
    <p><u><b>11. Can accredited investors invest under Regulation D offerings?</u></b><br>
    •Answer: Yes, they commonly invest under Regulation D Rules 506(b) and 506(c).
    </p>
    <p><u><b>12. How do accredited investors differ from sophisticated investors?</u></b><br>
    •Answer: Accredited investors meet financial thresholds, while sophisticated investors qualify based on experience and knowledge.
    </p>
    <p><u><b>13. What risks do accredited investors face in private equity?</u></b><br>
    •Answer: Risks include illiquidity, long holding periods, limited transparency, and potential capital loss.
    </p>
    <p><u><b>14. What are the benefits of private equity investing for accredited investors?</u></b><br>
    •Answer: Benefits include access to high-growth opportunities, diversification, and higher return potential.
    </p>
    <p><u><b>15. When should accredited investors consider private equity securities?</u></b><br>
    •Answer: Accredited investors should consider private equity when they have long-term investment horizons and high risk tolerance.
    </p>
    """)
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privateequitysecuritiesaccreditedinvestorstwelve(request):
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
    Capital Type: Accredited Investors</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    Equity capital from accredited investors is best suited for early-stage through growth-stage companies, including pre-seed, seed, and expansion phases. These investors are commonly the first source of external capital and can support companies before institutional venture capital becomes accessible. Your stage: {stage}
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    C-Corporations are the preferred entity type for raising equity from accredited investors, particularly for venture-backed companies seeking scalable growth. LLCs may also raise accredited investor capital, especially in operating or asset-based businesses. Sole proprietorships are generally not suitable due to ownership and securities law constraints. Your entity: {entity}
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Companies raising capital from accredited investors often have limited to moderate prior funding, such as founder capital, friends-and-family investments, or early angel participation. A clean cap table and clear ownership structure are important to maintain flexibility for future institutional rounds. Your prior capital: {preraise}
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    Accredited investor equity operates within the private capital markets and is commonly accessed through angel networks, family offices, high-net-worth individuals, and private investment groups rather than public markets. Your market type: {premarket}
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Capital raised from accredited investors typically ranges from $100,000 to tens of millions of dollars, depending on company stage, traction, and investor network depth. These raises are generally smaller than late-stage institutional rounds. Your goal: {raisegoal}
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Accredited investor offerings are often structured as pre-seed, seed, Series A, or growth equity rounds. Securities may include common stock, preferred equity, or hybrid equity instruments depending on investor preferences. Your round: {tranch}
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funds may be raised in a single close or through rolling closes as individual accredited investors commit capital over time. Rolling structures are common due to relationship-driven deal sourcing. Your tranches: {rounds}
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Proceeds are typically used for product development, hiring, market expansion, operating expenses, acquisitions, or general corporate purposes. Use of funds is generally flexible but must align with investor disclosures. Your use: {useoffund}
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Investor risk is high due to early-stage execution risk, illiquidity, and limited exit visibility. For issuers, risks include dilution, investor expectation management, and cap table complexity if many small investors are involved.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    The cost of capital is primarily equity dilution and the granting of investor rights such as information or governance provisions. There are no repayment obligations, but long-term ownership implications are significant. Your cost: {enterprisecost}
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are low to moderate and include legal structuring, securities filings, shareholder agreements, and administrative expenses. Costs increase with offering complexity and the number of investors. Your upfront cost: {upfrontcost}
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Timing to capital is relatively fast compared to institutional fundraising and often ranges from a few weeks to two months, depending on investor readiness and legal preparation. Your timeline: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction': introduction,
    }
    return render(request, 'detail.html', context)