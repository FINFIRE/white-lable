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
def privatedebtpromissorynote(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Promissory Note </center></p>
    <p><b><u>Introduction</u></b><br>
A Promissory Note is ideal for companies seeking a direct, legally binding debt arrangement with private lenders, investors, or even family and friends. It is designed so that a borrower can receive a specific sum of capital in exchange for a written promise to pay it back under defined terms, without the complex overhead of a full-scale commercial bank loan. {n} fits that definition. Promissory notes are among the oldest financial instruments in existence, predating modern banking systems. In 2026, they remain a vital tool for "bridge financing"—helping companies cover gaps between larger funding rounds. While a bank loan involves hundreds of pages of covenants, a promissory note can be a concise document that focuses on the "Three Rs": Rate, Repayment, and Recourse. On average, private promissory notes for mid-market businesses carry interest rates between 8% and 15%, with durations ranging from 6 months to 3 years. While promissory notes offer speed and extreme flexibility in deal-making, the risk of high interest rates, personal liability for the founder, and strict "default" clauses mean they must be drafted with precise legal care to avoid unintentional predatory terms.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Promissory Note is a "negotiable instrument" containing a written promise by one party (the issuer or maker) to pay another party (the payee) a definite sum of money, either on demand or at a specified future date. In the private debt market, these notes are typically "unsecured," meaning they are backed only by the creditworthiness of the company, or "secured" by specific assets like equipment or inventory. (Investopedia, 2026)
<br>


    <br>2.  The best type of companies to raise capital via promissory notes are those needing quick, short-term liquidity for specific projects. This includes real estate "fix-and-flip" ventures, startups bridging the gap to a Series A round, or established businesses funding a large purchase order. Because the terms are negotiated directly between the borrower and the lender, the business can often secure "interest-only" periods or "balloon payments" that wouldn't be possible at a traditional bank. (Forbes, 2025)
<br>

    <br>3. Promissory notes emerged in the 17th century through the London goldsmiths, eventually becoming formalized under the Uniform Commercial Code (UCC). In the modern era, the rise of "Private Credit" funds has revitalized the promissory note as a sophisticated instrument for high-yield investors looking for alternatives to the volatile stock market. In 2026, many of these notes are now being digitized through "Smart Contracts" to automate interest payments. (Uniform Law Commission, 2025)
<br>

    <br>4.While notes are easier to obtain than bank loans, they carry "predatory and legal" risks. In private debt, there is no federal cap on interest rates (other than state Usury Laws), leading some desperate borrowers to accept "hard money" terms that become mathematically impossible to repay. Furthermore, a promissory note often contains an "Acceleration Clause," which allows the lender to demand the entire balance immediately if the borrower misses a single payment or breaches a minor term. (Nolo, 2025)
<br>

    <br>5.
To raise capital via a promissory note, the company must issue a "Private Placement" or a direct debt offer. Unlike public bonds, these are private transactions. The note must specify whether it is Amortized (equal payments over time) or Balloon (small payments with a large final lump sum). For the note to be legally enforceable and professional, it should be accompanied by a "Security Agreement" if assets are being pledged as collateral. (LawDepot, 2026)
    </p>

    <p><u><b>References</u></b><br>
    <br>Investopedia.. Investopedia. (2026, Jan 02). Promissory Note: What It Is, Different Types, and How They Work.. <a href="https://www.investopedia.com/terms/p/promissorynote.asp">https://www.investopedia.com/terms/p/promissorynote.asp</a>
<br>

    <br>Forbes.. Forbes. (2025, Sept 14). Why Small Businesses Use Promissory Notes for Growth.. <a href="https://www.forbes.com/advisor/business-loans/promissory-notes/">https://www.forbes.com/advisor/business-loans/promissory-notes/</a>
<br>

    <br>Uniform Law Commission. (2025). Uniform Commercial Code Article 3: Negotiable Instruments. <a href="https://www.uniformlaws.org/">https://www.uniformlaws.org/</a>
<br>

    <br>Nolo. (2025). Promissory Notes for Personal and Business Loans. <a href="https://www.nolo.com/legal-encyclopedia/promissory-notes-personal-business-loans-30154.html">https://www.nolo.com/legal-encyclopedia/promissory-notes-personal-business-loans-30154.html</a>
<br>

    <br>LawDepot. (2026). Promissory Note Law and Enforcement. <a href="https://www.lawdepot.com/resources/business-articles/promissory-note/">https://www.lawdepot.com/resources/business-articles/promissory-note/</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   State Usury Compliance – The interest rate must not exceed the legal limit set by the state where the loan is issued.
<br>•   Securities Law Exemption – If issuing notes to multiple investors, you must often file for a Reg D exemption to avoid "illegal public offering" charges.
<br>•   Corporate Authorization – The note must be signed by an officer authorized by the Board of Directors or Operating Agreement.
<br>•   Negotiability Requirements – To be legally valid under the UCC, the note must be in writing, signed, and for a "sum certain" of money.
<br>•   UCC-1 Filing – If the note is "Secured," the lender must file a public lien to establish priority over other creditors.
<br>•   Accredited Investor Verification – If the lender is an individual, the company must often verify they are "accredited" to avoid regulatory scrutiny.


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   The Executed Promissory Note – The core document signed by both parties.
<br>•   Security Agreement – (Required only for secured notes) Detailing the collateral being pledged.
<br>•   UCC-1 Financing Statement – The public notice of the lender's lien on business assets.
<br>•   Corporate Resolution – A document proving the business has the authority to take on this debt.
<br>•   Personal Guarantee – A separate document if the founder is backing the note with personal assets.
<br>•   Amortization Schedule – A table showing exactly when and how each payment is applied to interest and principal.
<br>•   W-9 Form – Collected from the lender so the business can issue 1099-INT forms for interest paid.

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtpromissorynotefaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Private Debt<br>
    Promissory Note</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What is a promissory note in private debt financing?</u></b><br>
    •Answer: A promissory note is a written legal agreement in which a borrower formally promises to repay a specific sum of money to a lender under defined terms, including interest rate, repayment schedule, and maturity date.
</p>

    <p><u><b>2. Who typically uses promissory notes for business financing?</u></b><br>
    •Answer: Startups, small businesses, and privately held companies often use promissory notes when borrowing from individuals, private investors, or related parties outside traditional banks.
</p>

    <p><u><b>3. How much funding can be raised through a promissory note?</u></b><br>
    •Answer: Funding amounts vary widely and depend on the lender relationship and borrower credibility, typically ranging from a few thousand dollars to several million dollars.
</p>

    <p><u><b>4. How quickly can capital be accessed through a promissory note?</u></b><br>
    •Answer: Capital can often be accessed quickly, sometimes within days, once terms are agreed upon and the promissory note is executed.
</p>

    <p><u><b>5. Are promissory notes secured or unsecured?</u></b><br>
    •Answer: Promissory notes can be either secured by collateral or unsecured, depending on lender requirements and negotiated terms.
</p>

    <p><u><b>6. What interest rates apply to promissory notes?</u></b><br>
    •Answer: Interest rates are negotiated between the parties and usually reflect higher risk than bank loans, often exceeding traditional commercial lending rates.
</p>

    <p><u><b>7. What repayment terms are common in promissory notes?</u></b><br>
    •Answer: Repayment terms may include lump-sum repayment, installment payments, interest-only periods, or balloon payments at maturity.
</p>

    <p><u><b>8. Do promissory notes require equity dilution?</u></b><br>
    •Answer: No, promissory notes are debt instruments and do not require giving up ownership or equity in the business.
</p>

    <p><u><b>9. Can promissory notes be used for any business purpose?</u></b><br>
    •Answer: Yes, they can be used for working capital, startup expenses, bridge financing, acquisitions, or other business needs.
</p>

    <p><u><b>10. What are the main advantages of using promissory notes?</u></b><br>
    •Answer: Advantages include flexible terms, fast funding, minimal regulatory requirements, and the ability to structure deals privately.
</p>

    <p><u><b>11. What risks are associated with promissory notes?</u></b><br>
    •Answer: Risks include high interest costs, personal guarantees, legal enforcement risk, and strained relationships if repayment issues arise.
</p>

    <p><u><b>12. Can promissory notes be combined with other financing methods?</u></b><br>
    •Answer: Yes, they are often combined with bank loans, SBA financing, equity investments, or owner capital to complete a funding round.
</p>

    <p><u><b>13. How do promissory notes differ from convertible notes?</u></b><br>
    •Answer: Promissory notes require repayment in cash, while convertible notes may convert into equity under specified conditions.
</p>

    <p><u><b>14. Are promissory notes legally enforceable?</u></b><br>
    •Answer: Yes, when properly drafted and executed, promissory notes are legally binding and enforceable contracts.
</p>

    <p><u><b>15. How can borrowers reduce risk when issuing promissory notes?</u></b><br>
    •Answer: Borrowers can reduce risk by clearly defining terms, ensuring realistic repayment schedules, obtaining legal review, and maintaining transparent communication with lenders.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def privatedebtpromissorynotetwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Private Debt</b></u><br>
    Capital Type: Promissory Note</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Promissory notes are suitable for idea-stage, startup, early-growth, and established businesses, as they rely more on the borrower–lender relationship than formal underwriting. They are commonly used when businesses are not yet eligible for bank financing (Investopedia, 2024).
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
This instrument can be used by sole proprietorships, partnerships, LLCs, and corporations, as long as the borrower has legal capacity to enter a binding debt agreement. Personal promissory notes are also common in small business contexts (Cornell Law School, n.d.).
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Formal financial history is not always required, but lenders typically assess trust, repayment ability, and personal creditworthiness. Collateral or co-signers may be requested to reduce risk (Investopedia, 2024).
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Promissory notes operate in the private capital market, often involving family, friends, angel lenders, or private investors rather than regulated financial institutions (Harvard Business Review, 2022).
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
These notes are best suited for small to mid-sized capital needs, typically ranging from a few thousand to several hundred thousand dollars, depending on lender capacity and risk tolerance (Entrepreneur, 2023).
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Promissory notes are debt-based financing and are not considered equity rounds. They may, however, be used as bridge financing prior to equity investment or institutional debt (Y Combinator, 2023).
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Funds are usually released in a single tranche upon execution of the note, although milestone-based disbursement can be structured if agreed by both parties (Cornell Law School, n.d.).
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Use of funds is flexible and defined within the agreement. Common uses include working capital, early operations, equipment purchases, or short-term cash flow needs (Entrepreneur, 2023).

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Risk is high for lenders and moderate to high for borrowers, as repayment is legally enforceable. Default can result in legal action, asset seizure, or damaged personal relationships (Investopedia, 2024).
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
Capital cost includes interest payments, which may be fixed or variable. Rates are often higher than bank loans due to increased risk and lack of institutional backing (Harvard Business Review, 2022).
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are low, typically limited to legal drafting or notarization fees, making promissory notes cost-effective compared to formal lending products (Cornell Law School, n.d.).
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing is fast, often ranging from a few days to two weeks, since approval depends solely on private negotiation rather than regulatory review (Entrepreneur, 2023).
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)