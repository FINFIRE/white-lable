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

def privateequitysecuritiessophisticatedindividuals(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Sophisticated Individuals </center></p>
    <p><b><u>Introduction</u></b><br>
    Sophisticated Individuals are ideal participants in private equity securities offerings where investors possess sufficient financial knowledge and experience to evaluate the merits and risks of unregistered investments. These offerings are designed so that capital may be raised from individuals who, while not necessarily accredited by wealth thresholds, are capable of making informed investment decisions without the protections of public registration. {n} fits that definition. In 2026, sophisticated individual investors continue to play a meaningful role in private placements, particularly in founder-led companies, early-stage ventures, real estate syndications, and closely held operating businesses. Securities laws recognize sophistication as a functional standard focused on understanding risk, valuation, and liquidity constraints rather than net worth alone. While access to private equity securities expands the investor base, it introduces heightened disclosure, suitability, and compliance risk. Issuers must ensure information parity, investor comprehension, and adherence to exemption requirements to avoid regulatory violations or rescission claims.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. Sophisticated Individuals are investors who possess sufficient knowledge and experience in financial and business matters to evaluate the risks and merits of a private securities offering, even if they do not meet formal accredited investor income or net-worth thresholds. (U.S. Securities and Exchange Commission, 2025)<br><br>
    2. Investments made by sophisticated individuals fall within the Private Equity Securities segment of the capital markets and are typically conducted under private placement exemptions such as Regulation D Rule 506(b) or Section 4(a)(2), rather than through public offerings. (SEC, 2025)<br><br>
    3. Legally, offerings to sophisticated individuals require issuers to provide enhanced disclosure equivalent to that required in registered offerings, including detailed risk factors, financial statements, and business information. Suitability is assessed on an investor-by-investor basis. (Practising Law Institute, 2025)<br><br>
    4. From a risk perspective, participation by sophisticated individuals introduces issuer liability and rescission risk if disclosures are incomplete or misleading. Investors face heightened liquidity risk, valuation uncertainty, and limited exit options due to resale restrictions. (Harvard Law School Forum, 2025)<br><br>
    5. From an accounting and process standpoint, capital raised from sophisticated individuals is recorded as Equity or Equity-Linked Securities, depending on instrument structure. The fundraising process is relationship-driven and often slower due to individualized diligence, education, and suitability verification. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    U.S. Securities and Exchange Commission (SEC). (2025). Accredited Investor and Sophistication Standards. https://www.sec.gov/smallbusiness<br>
    Practising Law Institute (PLI). (2025). Private Placements and Investor Sophistication. https://www.pli.edu<br>
    Harvard Law School Forum on Corporate Governance. (2025). Private Offering Exemptions and Risk. https://corpgov.law.harvard.edu<br>
    Deloitte. (2025). Accounting for Private Equity Issuances. https://www2.deloitte.com/equity<br>
    CFA Institute. (2025). Investor Suitability and Private Markets. https://www.cfainstitute.org
    </p>
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Investor Sophistication – Demonstrated financial and investment knowledge<br>
    • Offering Exemption – Regulation D 506(b) or Section 4(a)(2)<br>
    • Enhanced Disclosure – Registered-offering–level information<br>
    • No General Solicitation – Prohibition on public advertising<br>
    • Investor Suitability Review – Individual risk assessment<br>
    • Resale Restrictions – Restricted securities subject to Rule 144<br>
    • Form D Filing – SEC exemption notice (if applicable)<br>
    • State Blue Sky Compliance – Notice filings and fees
    </p>
    <p><b><u>Supporting Document List</b></u><br>
    • Private Placement Memorandum (PPM) – Offering disclosures<br>
    • Subscription Agreement – Investor commitments and representations<br>
    • Investor Questionnaire – Sophistication and suitability confirmation<br>
    • Financial Statements – Issuer performance disclosures<br>
    • Capitalization Table – Ownership structure<br>
    • Form D Filing – SEC notice (if applicable)<br>
    • Board & Shareholder Resolutions – Authorization to issue securities<br>
    • Legal Opinions – Exemption and compliance confirmation
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiessophisticatedindividualsfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Sophisticated Individuals</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. Who are sophisticated individuals in private equity investing?</u></b><br>
    • Answer: Sophisticated individuals are investors who have sufficient financial knowledge and experience to understand and evaluate private equity investments and their risks.
    </p>
    <p><u><b>2. Are sophisticated individuals the same as accredited investors?</u></b><br>
    • Answer: No, sophisticated individuals may not meet accredited investor income or net-worth thresholds but are deemed capable of assessing investment risks.
    </p>
    <p><u><b>3. When are sophisticated individuals allowed to invest in private equity securities?</u></b><br>
    • Answer: They may invest in specific private offerings, such as Regulation D Rule 506(b), where limited participation by non-accredited but sophisticated investors is permitted.
    </p>
    <p><u><b>4. What criteria determine whether an individual is sophisticated?</u></b><br>
    • Answer: Criteria include investment experience, financial literacy, professional background, and ability to evaluate complex financial information.
    </p>
    <p><u><b>5. Is formal certification required to qualify as a sophisticated individual?</u></b><br>
    • Answer: No formal certification is required; issuers determine sophistication through disclosures, questionnaires, or interviews.
    </p>
    <p><u><b>6. Are there limits on how many sophisticated individuals can invest in one offering?</u></b><br>
    • Answer: Yes, under Rule 506(b), up to 35 non-accredited but sophisticated investors may participate.
    </p>
    <p><u><b>7. What disclosure requirements apply for sophisticated individuals?</u></b><br>
    • Answer: Issuers must provide detailed disclosures similar to those required in registered securities offerings.
    </p>
    <p><u><b>8. Are securities sold to sophisticated individuals restricted?</u></b><br>
    • Answer: Yes, these securities are restricted and cannot be freely resold without meeting regulatory exemptions.
    </p>
    <p><u><b>9. What risks do sophisticated individuals face in private equity investments?</u></b><br>
    • Answer: Risks include illiquidity, long holding periods, limited transparency, and potential loss of invested capital.
    </p>
    <p><u><b>10. What benefits do sophisticated individuals gain from private equity investing?</u></b><br>
    • Answer: Benefits include access to private companies, early-stage investments, and higher potential returns.
    </p>
    <p><u><b>11. Do sophisticated individuals receive the same regulatory protections as retail investors?</u></b><br>
    • Answer: No, they receive fewer protections because they are assumed to understand and accept higher investment risks.
    </p>
    <p><u><b>12. Can sophisticated individuals invest alongside accredited and institutional investors?</u></b><br>
    • Answer: Yes, they commonly invest alongside accredited investors and institutions in private placements.
    </p>
    <p><u><b>13. How do issuers verify investor sophistication?</u></b><br>
    • Answer: Verification is done through investor questionnaires, financial background checks, and assessment of investment experience.
    </p>
    <p><u><b>14. How do sophisticated individuals differ from institutional investors?</u></b><br>
    • Answer: Sophisticated individuals invest personal capital, while institutional investors invest pooled or fiduciary funds.
    </p>
    <p><u><b>15. When should sophisticated individuals consider investing in private equity securities?</u></b><br>
    • Answer: They should consider investing when they have adequate risk tolerance, long-term investment horizons, and a strong understanding of private market risks.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def privateequitysecuritiessophisticatedindividualstwelve(request):
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
    Capital Type: Sophisticated Individuals</p></center>
    <p><b><u>1 – Stage of Development Assessment</b></u><br>
    Equity capital from sophisticated individuals is best suited for early-stage through growth-stage companies, particularly during pre-seed, seed, and early expansion phases. These investors often engage before institutional venture capital and are comfortable with higher risk in exchange for early access and potential upside. {stage} aligns with this profile.
    </p>
    <p><b><u>2 – Entity Type Assessment</b></u><br>
    C-Corporations are the preferred entity type for raising equity from sophisticated individuals, especially for startups anticipating future institutional investment. LLCs may also be used in certain operating or real estate contexts. Sole proprietorships are generally not suitable due to ownership, liability, and securities compliance considerations. {{entity}} is {{entity}} appropriate.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</b></u><br>
    Companies raising from sophisticated individuals typically have limited prior capital, such as founder funding or friends-and-family investment. While prior fundraising does not disqualify issuers, early dilution and cap table structure must remain clean to support future institutional rounds. {{preraise}} reflects {{preraise}} typical prior capital.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</b></u><br>
    This form of financing operates within the private early-stage investment market and is driven by angel investors, high-net-worth individuals, operators, executives, and former founders investing personal capital rather than institutional funds. {{premarket}} reflects {{premarket}} market positioning.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</b></u><br>
    Capital raised from sophisticated individuals typically ranges from $50,000 to several million dollars, depending on the size of the investor network, company traction, and stage of development. These raises are generally smaller than institutional venture rounds. {{raisegoal}} aligns with typical ranges.
    </p>
    <p><b><u>6 – Capital Round Assessment</b></u><br>
    Investments from sophisticated individuals are often structured as pre-seed or seed equity rounds, or as early Series A participation. Investments may be made through common stock, preferred equity, or simple equity instruments. {{tranch}} represents {{tranch}} structure.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</b></u><br>
    Funds may be raised in a single close or through rolling closes as individual investors commit capital at different times. Rolling structures are common due to relationship-driven deal flow. {{rounds}} reflects {{rounds}} approach.
    </p>
    <p><b><u>8 – Use of Funds Assessment</b></u><br>
    Proceeds are typically used for product development, early hiring, market validation, operating expenses, and preparing for institutional fundraising. Use of funds is generally flexible but aligned with investor expectations and disclosures. {{useoffund}} represents {{useoffund}} typical uses.
    </p>
    <p><b><u>9 – Risk Assessment</b></u><br>
    Investor risk is high due to early-stage execution risk, illiquidity, and limited governance protections. For founders, risks include cap table complexity, misaligned expectations, and governance challenges if too many small investors are involved.
    </p>
    <p><b><u>10 – Capital Cost Assessment</b></u><br>
    The cost of capital is primarily equity dilution and potential governance or information rights granted to investors. While there is no repayment obligation, long-term ownership and control considerations represent meaningful costs. {{enterprisecost}} reflects {{enterprisecost}} cost profile.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</b></u><br>
    Upfront costs are low to moderate and include legal structuring, shareholder agreements, securities compliance filings, and administrative setup. Costs increase if multiple investors require individualized documentation or side letters. {{upfrontcost}} is {{upfrontcost}} typical.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</b></u><br>
    Timing to capital is relatively fast compared to institutional rounds and often ranges from a few weeks to two months, depending on investor relationships, legal readiness, and deal structure. {{upfronttime}} reflects {{upfronttime}} expected timeline.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
