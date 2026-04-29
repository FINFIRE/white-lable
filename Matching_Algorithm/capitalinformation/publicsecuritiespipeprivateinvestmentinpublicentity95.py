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

def publicsecuritiespipeprivateinvestmentinpublicentity(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities</b></u><br>
    Capital Type: PIPE Private Investment in Public Entity </center></p>
    <p><b><u>Introduction</u></b><br>
    A Private Investment in Public Equity (PIPE) is a financing transaction in which a publicly traded company sells securities directly to accredited investors in a private placement rather than through a public offering. {n} fits that definition. PIPE transactions allow public companies to raise capital quickly and efficiently, often at a negotiated discount to market price. These transactions are typically structured under exemptions provided by the Securities Act of 1933 and are regulated by the U.S. Securities and Exchange Commission. PIPEs are frequently used by companies seeking growth capital, restructuring funds, or acquisition financing.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    1. A PIPE transaction involves the private sale of common stock, preferred stock, or convertible securities by a public company to institutional or accredited investors. Because the offering is private, it is typically conducted under Regulation D exemptions and does not require immediate SEC registration. However, companies often agree to file a resale registration statement to allow investors to publicly resell the securities after closing. PIPEs are commonly used for speed, confidentiality, and reduced underwriting costs compared to traditional public offerings.<br>
    <br>
    2. PIPE financing is best suited for publicly traded companies that require rapid access to capital without the delays associated with secondary public offerings. It is frequently used by small-cap or mid-cap public companies, distressed companies, and companies emerging from mergers, including those formed through SPAC transactions. Investors in PIPEs typically include hedge funds, private equity firms, and institutional investors seeking discounted entry into public equity positions.<br>
    <br>
    3. PIPE offerings are generally structured under Regulation D of the Securities Act of 1933, which permits private placements to accredited investors without full SEC registration. Although the initial issuance is exempt, resale registration statements are often filed with the SEC to provide liquidity. Public companies must also comply with ongoing disclosure obligations under the Securities Exchange Act of 1934. Exchange rules from markets such as NASDAQ or New York Stock Exchange may require shareholder approval if issuance exceeds certain thresholds.<br>
    <br>
    4. PIPE transactions often involve issuing shares at a discount to market price, which may result in dilution for existing shareholders. Announcement of a PIPE may negatively impact stock price due to perceived financial distress. Investors face liquidity risk until resale registration becomes effective. Additionally, convertible or structured PIPEs may lead to downward price pressure if investors hedge or short the underlying stock.<br>
    <br>
    5. To successfully execute a PIPE transaction, a public company must demonstrate credible financial performance, transparent disclosures, and a clear capital deployment strategy. Companies must negotiate pricing, lock-up terms, registration rights, and investor protections. Legal counsel prepares subscription agreements, registration rights agreements, and SEC filings. Strong institutional investor relationships and market confidence significantly increase the likelihood of successful placement.
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Compliance with Regulation D under the Securities Act of 1933<br>
    · Accredited Investor Participation<br>
    · Public Company Reporting Compliance under the Securities Exchange Act of 1934<br>
    · Exchange Shareholder Approval (if required)<br>
    · SEC Resale Registration Filing (Form S-1 or S-3)<br>
    · Corporate Board Authorization<br>
    · AML/KYC Compliance
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · Private Placement Memorandum (if used)<br>
    · Subscription Agreement<br>
    · Registration Rights Agreement<br>
    · Form D Filing<br>
    · SEC Resale Registration Statement<br>
    · Board Resolutions Authorizing Issuance<br>
    · Updated Capitalization Table<br>
    · Risk Disclosure Statement<br>
    · Legal Opinion Letter
    </p>
    <p><u><b>References</b></u><br>
    1. U.S. Securities and Exchange Commission. (2023). Private Placements and Regulation D. https://www.sec.gov/smallbusiness/exemptofferings/regd<br>
    2. Securities Act of 1933. https://www.sec.gov/about/laws/sa33.pdf<br>
    3. Securities Exchange Act of 1934. https://www.sec.gov/about/laws/sea34.pdf<br>
    4. NASDAQ. (n.d.). Listing Rules and Shareholder Approval Requirements. https://listingcenter.nasdaq.com<br>
    5. Investopedia. (n.d.). PIPE (Private Investment in Public Equity) Definition. https://www.investopedia.com/terms/p/pipe.asp
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiespipeprivateinvestmentinpublicentityfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities<br>
    PIPE Private Investment in Public Entity</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is a PIPE transaction?</u></b><br>
    • Answer: A Private Investment in Public Equity (PIPE) is a financing method where private investors purchase shares of a publicly traded company at a negotiated price, typically at a discount to market value.
    </p>
    <p><u><b>2. How does a PIPE transaction work?</u></b><br>
    • Answer: A public company issues new shares or convertible securities directly to accredited investors through a private placement rather than a public offering.
    </p>
    <p><u><b>3. Who participates in PIPE deals?</u></b><br>
    • Answer: Participants typically include institutional investors, hedge funds, private equity firms, and accredited investors.
    </p>
    <p><u><b>4. Why do companies use PIPE financing?</u></b><br>
    • Answer: Companies use PIPE financing to raise capital quickly with fewer regulatory requirements compared to a traditional public offering.
    </p>
    <p><u><b>5. What types of securities are issued in PIPE deals?</u></b><br>
    • Answer: PIPE transactions may involve common stock, preferred stock, convertible notes, or warrants.
    </p>
    <p><u><b>6. Is a PIPE offering registered with regulators?</u></b><br>
    • Answer: The initial sale is conducted as a private placement under exemptions regulated by the U.S. Securities and Exchange Commission, with shares typically registered for resale later.
    </p>
    <p><u><b>7. What is the advantage of PIPE financing?</u></b><br>
    • Answer: Advantages include speed, lower transaction costs, and access to institutional capital without extensive public roadshows.
    </p>
    <p><u><b>8. What are the risks of PIPE financing?</u></b><br>
    • Answer: Risks include shareholder dilution, discounted share pricing, and potential downward pressure on stock price.
    </p>
    <p><u><b>9. How does a PIPE differ from a public secondary offering?</u></b><br>
    • Answer: A PIPE is privately negotiated with select investors, while a secondary offering is marketed broadly to the public.
    </p>
    <p><u><b>10. Does PIPE financing dilute existing shareholders?</u></b><br>
    • Answer: Yes, issuing new shares or convertible securities can dilute existing ownership percentages.
    </p>
    <p><u><b>11. Can PIPE financing be used with SPAC transactions?</u></b><br>
    • Answer: Yes, PIPE investments are commonly used alongside mergers involving Special Purpose Acquisition Companies to provide additional capital.
    </p>
    <p><u><b>12. How quickly can a PIPE transaction close?</u></b><br>
    • Answer: PIPE deals can close relatively quickly, often within a few weeks, compared to traditional public offerings.
    </p>
    <p><u><b>13. Are PIPE investors subject to holding periods?</u></b><br>
    • Answer: Yes, securities are typically restricted until resale registration becomes effective.
    </p>
    <p><u><b>14. What is a structured PIPE?</u></b><br>
    • Answer: A structured PIPE includes convertible or adjustable securities that may have price reset features tied to market performance.
    </p>
    <p><u><b>15. When should a company consider PIPE financing?</u></b><br>
    • Answer: A company should consider PIPE financing when seeking efficient capital infusion while maintaining public market status.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiespipeprivateinvestmentinpublicentitytwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Public Securities</b></u><br>
    Capital Type: PIPE Private Investment in Public Entity</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    PIPE financing is best suited for:<br>
    · Public companies needing growth capital<br>
    · Post-SPAC merger entities<br>
    · Micro-cap and small-cap public issuers<br>
    · Companies seeking faster capital than a traditional follow-on offering<br>
    It is commonly used when market conditions make traditional public offerings difficult.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Applicable to:<br>
    · Publicly traded C-Corporations<br>
    · Exchange-listed or OTC-traded companies<br>
    · SPAC-combined operating companies<br>
    Issuer must already be subject to reporting requirements under the U.S. Securities and Exchange Commission.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Before launching a PIPE, companies typically need:<br>
    · Current SEC filings (10-K, 10-Q, 8-K as applicable)<br>
    · Audited financial statements<br>
    · Defined use of proceeds<br>
    · Institutional investor outreach strategy<br>
    · Board approval<br>
    Legal counsel prepares subscription agreements and registration rights agreements.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    PIPE transactions are structured as private placements under securities exemptions (commonly Regulation D) but involve public company securities.
    Although privately negotiated, securities are typically registered for resale after closing through SEC filings.
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    PIPE transactions commonly range from:<br>
    · $5 million to $250+ million, depending on issuer size<br>
    · Larger PIPEs are often associated with SPAC merger transactions<br>
    Institutional investors usually participate.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Common PIPE structures include:<br>
    · Common stock at a discount<br>
    · Convertible preferred stock<br>
    · Convertible notes<br>
    · Structured equity with warrants<br>
    Pricing is often discounted relative to current market price.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Capital may be raised:<br>
    · In a single closing<br>
    · In milestone-based tranches<br>
    · As part of a SPAC business combination<br>
    Funds are typically wired at closing.
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Common uses include:<br>
    · Working capital<br>
    · Debt repayment<br>
    · Acquisition financing<br>
    · Expansion initiatives<br>
    · Strengthening balance sheet<br>
    Use of proceeds must be disclosed publicly.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk level: Moderate to High<br>
    Risks include:<br>
    · Shareholder dilution<br>
    · Downward pressure on stock price<br>
    · Convertible security overhang<br>
    · Regulatory compliance exposure<br>
    Market reaction can impact valuation post-announcement.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Capital costs may include:<br>
    · Discounted share pricing (often 5%–20%)<br>
    · Warrant coverage<br>
    · Placement agent fees (typically 4%–8%)<br>
    · Legal and filing costs<br>
    Effective cost can be high due to dilution impact.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are moderate to high, including:<br>
    · Legal documentation<br>
    · SEC registration statements (for resale)<br>
    · Placement agent engagement fees<br>
    · Financial updates<br>
    Preparation time is shorter than a traditional public offering.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    PIPE transactions are relatively fast, typically closing within 4–8 weeks, depending on:<br>
    · Investor demand<br>
    · Negotiation terms<br>
    · SEC resale registration process<br>
    Faster than most public follow-on offerings.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
