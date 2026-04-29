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

def privateequitysecuritiesconvertiblenote(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Convertible Note </center></p>
    <p><b><u>Introduction</u></b><br>
    A Convertible Note is ideal for early-stage companies that need to raise capital quickly but are not yet ready to set a formal valuation. It is designed so that the investment starts as a short-term debt instrument that later converts into equity (typically preferred stock) during a future "priced" financing round. {n} fits that definition. In 2026, convertible notes remain a staple of the "Seed" and "Bridge" financing markets. While the SAFE (Simple Agreement for Future Equity) has become the standard for very early software startups, convertible notes are often preferred by institutional investors and companies in capital-intensive sectors like Biotech, Hardware, and Medical Devices because they offer more structured protection. On average, these notes carry a maturity of 18 to 24 months and an interest rate of 4% to 8%. The global market for these hybrid instruments has remained robust, providing a "bridge" for companies to reach major milestones before a Series A. While convertible notes delay the "valuation tug-of-war" between founders and investors, the primary risk is the "Maturity Wall." If a company fails to raise a qualifying round before the note expires, the investor can legally demand full repayment of the principal plus interest, which can force a cash-strapped startup into insolvency or a predatory renegotiation.
    </p>
    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1. A Convertible Note is a hybrid security that shares characteristics of both debt and equity. It is a loan that is intended to be repaid with shares rather than cash. The "magic" of the note lies in its Conversion Triggers—automatic events, such as raising a minimum of $1M in a new equity round, that force the debt to turn into ownership. (Exbo Group, 2026)<br>
    <br>2. The best type of companies to use convertible notes are those that have a clear path to a larger institutional round within 12–24 months. Because they are technically debt, they sit higher in the "Capital Stack" than equity, providing investors with downside protection. In the event of a liquidation, noteholders are usually paid back before any common or preferred shareholders. (British Business Bank, 2025)<br>
    <br>3. The modern structure of the convertible note was popularized in Silicon Valley but has since become globally standardized. In 2026, "Mandatory Convertibles" have gained traction, where the note must convert at maturity even if a financing round hasn't occurred, preventing the "repayment shock" for founders while ensuring the investor gets their equity stake. (Corporate Finance Institute, 2026)<br>
    <br>4. While the note provides speed, it carries "Dilution and Accounting" risks. Because interest accrues and is added to the principal, the eventual equity stake of the investor grows every month the note remains outstanding. On the balance sheet, these notes appear as a Liability, which can sometimes complicate traditional bank lending or credit checks until they are converted. (Wall Street Prep, 2025)<br>
    <br>5. To raise capital via a Convertible Note, the legal process is significantly cheaper and faster than a priced round. Instead of rewriting the company's charter (Articles of Incorporation), parties sign a Note Purchase Agreement and a Promissory Note. In 2026, many of these transactions are executed via digital equity management platforms (like Carta or Pulley), which automatically track interest and calculate the "cap table" impact of conversion. (Velawood, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Exbo Group. (2026, Jan 10). Convertible Notes: A Strategic Tool for Early-Stage Financing. https://www.exbogroup.com/article/convertible-notes<br>
    British Business Bank. (2025, Oct 09). What are Convertible Loan Notes? https://www.british-business-bank.co.uk/finance-hub/convertible-loan-notes/<br>
    Corporate Finance Institute (CFI). (2026). Convertible Note: Overview, Terms, and Advantage. https://corporatefinanceinstitute.com/resources/fixed-income/convertible-note/<br>
    Wall Street Prep. (2025, July 15). Convertible Note Definition and Lending Examples. https://www.wallstreetprep.com/knowledge/convertible-note/<br>
    Velawood Law. (2025, Oct 09). The Basics of Convertible Notes for Emerging Companies. https://velawood.com/the-basics-of-convertible-notes/
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Accredited Investor Verification – To comply with SEC Regulation D, investors must meet specific wealth or income thresholds.<br>
    · Qualified Financing Trigger – The legal definition of what "size" of future round (e.g., $1M+) will trigger the conversion.<br>
    · Valuation Cap – A contractually agreed-upon "ceiling" that ensures early investors aren't overly diluted if the company's value skyrockets.<br>
    · Conversion Discount – Typically 15% to 25%, giving the noteholder a lower price per share than new investors.<br>
    · Maturity Date – The legal "deadline" (usually 18-24 months) for conversion or repayment.<br>
    · Board & Shareholder Consent – Formal corporate resolutions authorizing the issuance of debt that can turn into shares.<br>
    · UCC Filing (Optional) – Some notes are "secured" by company assets, requiring a public lien filing, though most are "unsecured."
    </p>
    <p><b><u>Supporting Document List</u></b><br>
    · Note Purchase Agreement (NPA) – The main contract governing the sale of the notes.<br>
    · Promissory Note – The legal "IOU" detailing the principal, interest, and maturity.<br>
    · Term Sheet – A summary of key conversion terms (Cap, Discount, Interest).<br>
    · Cap Table (Pro-Forma) – A model showing what ownership looks like after conversion at different valuations.<br>
    · Board Resolutions – Approval minutes from the Board of Directors.<br>
    · Shareholder Consent – Approval from existing equity holders to allow for future dilution.<br>
    · Disclosure Schedules – A list of current company liabilities and legal status.
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privateequitysecuritiesconvertiblenotefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Equity Securities<br>
    Convertible Note</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is a convertible note?</u></b><br>
    •Answer: A convertible note is a short-term debt instrument that converts into equity at a later financing round, rather than being repaid in cash.
    </p>
    <p><u><b>2. When are convertible notes typically used?</u></b><br>
    •Answer: Convertible notes are commonly used in pre-seed and seed funding rounds when a company's valuation is not yet clearly established.
    </p>
    <p><u><b>3. How does a convertible note convert into equity?</u></b><br>
    •Answer: The note converts into equity during a future qualified financing round, usually at a discounted price or with a valuation cap.
    </p>
    <p><u><b>4. What is a valuation cap in a convertible note?</u></b><br>
    •Answer: A valuation cap sets the maximum company valuation at which the note will convert, protecting early investors from excessive dilution.
    </p>
    <p><u><b>5. What is a discount rate in a convertible note?</u></b><br>
    •Answer: The discount rate allows note holders to convert their investment into equity at a lower price than new investors in the next round.
    </p>
    <p><u><b>6. Do convertible notes earn interest?</u></b><br>
    •Answer: Yes, convertible notes typically accrue interest, which is added to the principal and converts into equity rather than being paid in cash.
    </p>
    <p><u><b>7. What is the maturity date of a convertible note?</u></b><br>
    •Answer: The maturity date is the deadline by which the note must either convert into equity, be repaid, or be renegotiated.
    </p>
    <p><u><b>8. Is collateral required for a convertible note?</u></b><br>
    •Answer: No, convertible notes are usually unsecured and do not require collateral.
    </p>
    <p><u><b>9. How much capital is typically raised through convertible notes?</u></b><br>
    •Answer: Amounts vary, but startups commonly raise between $50,000 and $2 million through convertible note financing.
    </p>
    <p><u><b>10. How do convertible notes benefit startups?</u></b><br>
    •Answer: They allow faster fundraising, defer valuation discussions, and involve simpler legal documentation compared to equity rounds.
    </p>
    <p><u><b>11. What are the benefits for investors using convertible notes?</u></b><br>
    •Answer: Investors gain downside protection as debt and upside potential through equity conversion at favorable terms.
    </p>
    <p><u><b>12. What are the risks associated with convertible notes?</u></b><br>
    •Answer: Risks include company failure before conversion, unclear conversion terms, or unfavorable future financing outcomes.
    </p>
    <p><u><b>13. Can multiple investors participate in a convertible note round?</u></b><br>
    •Answer: Yes, startups often raise convertible notes from multiple investors under the same or similar terms.
    </p>
    <p><u><b>14. How does a convertible note differ from a SAFE?</u></b><br>
    •Answer: Unlike SAFEs, convertible notes are debt instruments with interest and maturity dates.
    </p>
    <p><u><b>15. When should a company use a convertible note?</u></b><br>
    •Answer: A company should consider a convertible note when it needs quick early-stage capital and expects a priced equity round in the future.
    </p>
    """)
    context = {
        'introduction':introduction,
    }
    return render(request, 'detail.html', context)

def privateequitysecuritiesconvertiblenotetwelve(request):
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
    Capital Type: Convertible Note</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    Convertible notes are best suited for early-stage startups, typically at the pre-seed to seed stage, when company valuation is still uncertain and speed of fundraising is important. Your stage: {stage}
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    C-Corps are the preferred entity type for issuing convertible notes. LLCs may be used in limited cases, but conversion mechanics and tax complexity make C-Corps the standard. Sole proprietorships are generally not suitable. Your entity: {entity}
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Convertible notes are commonly used when a company has raised little or no institutional equity. Founder capital and friends-and-family funding are acceptable, but excessive prior equity dilution may complicate note terms. Your prior capital: {preraise}
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    Convertible notes operate within the private early-stage investment market, commonly used by angel investors, seed funds, and early venture capital firms. Your market type: {premarket}
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    Convertible note rounds typically range from $100,000 to $3,000,000, depending on investor appetite, traction, and expected future valuation. Your goal: {raisegoal}
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    Convertible notes are typically used in pre-seed or seed rounds and are intended to convert into equity during a future priced round, such as a Series A. Your round: {tranch}
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    Funds are often raised in a single tranche, though rolling closes may occur as additional investors join before the note maturity date. Your tranches: {rounds}
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    Funds are generally used for: Product development, Market validation, Hiring core team members, Preparing for a priced equity round. Use of funds is flexible but focused on accelerating growth. Your use: {useoffund}
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk is very high for investors due to startup failure risk. For founders, risk includes future dilution, valuation caps, and repayment obligations if conversion does not occur.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    The cost of capital includes equity dilution upon conversion, interest accrual, and potential valuation discounts or caps favoring investors. Your cost: {enterprisecost}
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are low to moderate, mainly consisting of legal drafting, note documentation, and administrative costs. Your upfront cost: {upfrontcost}
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    Timing to capital is relatively fast, often 4–8 weeks, making convertible notes a popular option for quick early-stage fundraising. Your timeline: {upfronttime}
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction': introduction,
    }
    return render(request, 'detail.html', context)