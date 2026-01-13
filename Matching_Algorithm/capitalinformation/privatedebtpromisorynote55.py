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


def privatedebtpromisorynote(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Debt</b></u><br>
    Capital Type: Promissory Note</center></p>
    
    <p><b><u>Introduction</u></b><br>
    It is probably the simplest representation of a debt. All you need to document on paper is who is lending to whom, the amount, the date of the transaction and when it should be paid back, and both signatures<a href="https://www.bdc.ca/en/articles-tools/entrepreneur-toolkit/templates-business-guides/glossary/promissory-note"> (source)</a>. Promissory notes are also flexible. They allow the parties involved to negotiate terms such as interest rates and repayment schedule to suit their individual needs and circumstances. Promissory notes can be an effective tool for raising capital. Business owners can use promissory notes to secure funding from individual investors, avoiding the need to obtain bank loans or issue bonds or shares. This can simplify the capital-raising process and potentially reduce transaction costs<a href="https://www.debitura.com/payment-terms/articles/pros-and-cons-of-a-promissory-note"> (source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) A promissory note is a financial document that contains a written promise by one party (the note's issuer or maker) to pay another party (the note's payee) a definite sum of money, either on demand or at a specified future date. A promissory note typically contains all the terms pertaining to the indebtedness, such as the principal amount, interest rate, maturity date, date and place of issuance, and issuer's signature. Although financial institutions may issue them, promissory notes are debt instruments that allow companies and individuals to get financing from a source other than a bank. This source can be an individual or a company willing to carry the note to provide the financing, under the agreed-upon terms. (Smith, 2021)

    <br><br>2) A promissory note typically contains all the terms involved, such as the principal debt amount, interest rate, maturity date, payment schedule, the date and place of issuance, and the issuer's signature.

    <br><br>Promissory notes can lie between an IOU's informality and a loan contract's rigidity. An IOU merely acknowledges a debt and the amount one party owes another. A promissory note includes a promise to pay on demand or at a specified future date, in addition to steps required for repayment (like the repayment schedule). In its simplest form, a promissory note might be a written promise to repay a family member. State or federal securities entities may regulate more complicated promissory notes.

    <br><br>A promissory note can be secured or unsecured. A secured promissory note describes the collateral—typically property—that secures the debt or amount borrowed. For example, if the borrower owns property, the lender can use the car as collateral until the debt is repaid. If the borrower doesn't repay the loan, the promissory note permits the lender to take possession of the property.
    <br>An unsecured promissory note doesn't involve collateral. In this case, if the borrower doesn't repay the loan, the lender can try to use standard debt-collection procedures.

    <br><br>In either case, the lender holds the promissory note until the debt is repaid. Typically, those drafting a promissory note will consult with an attorney to make sure the note follows any state or federal laws around loans or investments. (Barone, 2024)

    3<br><br>) With promissory notes, it’s possible to create a secured promissory note (backed by collateral or assets) or an unsecured promissory note, depending on the type of debt.

    <br><br>Regardless of the type, here’s what a promissory note typically contains: 
    <br>Identification - Full names and addresses of the maker and payee. 
    <br>Loan details - The amount borrowed, interest rate (if applicable), and repayment terms, including the payment schedule and maturity date. 
    <br>Security or collateral - Description of assets used to secure the loan (not applicable to unsecured promissory notes).
    <br>Default and late payment terms - Conditions that constitute a loan default and any penalties for late payments. 
    <br>Prepayment terms - Information on early repayment options and any associated fees. 
    <br>Signatures and dates - Both parties must sign and date the document for it to be legally binding. 

    <br><br>Like other legal documents, promissory notes typically contain miscellaneous terms or sections, such as clauses for how to handle disputes. It’s also a good idea to notarize the note, especially for informal agreements that are more likely to be disputed. (Almadrones, 2024) 

    <br><br>4) Someone who fails to repay a loan detailed in a promissory note can lose an asset that secures the loan, such as a home, or face other actions.

    <br><br>First, you should ask for the repayment in writing. Past due notices are commonly sent at 30, 60, and 90 days after the stated due date.

    <br><br>If the borrower still does not pay you back, you might consider asking your borrower to make a partial payment. You can create a debt settlement agreement if you decide to accept partial repayment of a debt. You may also consider creating an extended payment plan that allows the borrower to pay you back in full over a revised period of time.

    <br><br>You can also choose to use a debt collector to obtain repayment. A debt collector works with you to collect the note, generally taking a percentage of the payment. Alternately, you can sell the note to a debt collector. Selling a note to a debt collector gives the debt collector ownership of the loan and the ability to collect the full amount. It is more common to assign debt to a debt collector, though.

    <br><br>If nothing else works, you can also sue your borrower for the full amount owed to you. (Promissory Note: Definition, When To Use, What's Included, n.d.)
    </p>
                             
    <u><b><p>References</u></b><br>
    Almadrones, M. (2024, September 23). What Is a Promissory Note? Definition, Examples, and Uses. Retrieved from Legal Zoom: <a href="https://www.legalzoom.com/articles/what-is-a-promissory-note">https://www.legalzoom.com/articles/what-is-a-promissory-note</a>
    <br><br>Barone, A. (2024, February 27). Promissory Note: What It Is, Different Types, and Pros and Cons. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/p/promissorynote.asp">https://www.investopedia.com/terms/p/promissorynote.asp</a>
    <br><br>Promissory Note: Definition, When To Use, What's Included. (n.d.). Retrieved from Contracts Counsel: <a href="https://www.contractscounsel.com/t/us/promissory-note">https://www.contractscounsel.com/t/us/promissory-note</a>
    <br><br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Business Entity Status - Must be a legally established entity (e.g., corporation, LLC, partnership).
    <br>• Authority to Borrow - Individuals signing the note must have legal authority to bind the business.
    <br>• Capacity to Contract - Business must have the legal capacity to enter into contracts (e.g., not in bankruptcy).
    <br>• Securities Laws Compliance - Must comply with federal and state securities laws, including registration or exemptions (e.g., Regulation D).
    <br>• Disclosure Requirements - Provide necessary disclosures to investors (e.g., terms, risks, financial condition).
    <br>• Interest Rate Compliance - Interest rate must comply with usury laws (limits on maximum rates).
    <br>• Tax Compliance - Comply with tax laws regarding interest deductibility and reporting.
    <br>• Investor Eligibility - Ensure investors meet eligibility requirements (e.g., accredited investors for private placements).
    <br>• Loan Terms and Agreement - Clearly outline loan terms (principal, interest, repayment schedule, security provisions).
    <br>• Ability to Repay and Financial Health - Business must have the financial capacity to repay the loan.
    <br>• Legal Review of Promissory Note - Have legal counsel review the promissory note to ensure compliance.
    <br>• Registration of Debt Instrument - May need to register the debt instrument with SEC or state agencies if required.
    <br>• Public Disclosure and Reporting (if applicable) - Public companies must adhere to public reporting requirements.
    </p>
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Promissory Note Agreement - A legally binding document outlining the terms of the loan, including the principal amount, interest rate, repayment schedule, maturity date, and any collateral or security provisions.
    <br>• Business Formation Documents - Articles of Incorporation or Certificate of Formation (for corporations or LLCs) along with Operating Agreement or Bylaws (for LLCs or corporations) to show the business's authority to borrow funds.
    <br>• Board or Member Approval Resolution - A formal resolution from the board of directors (corporation) or members (LLC) authorizing the issuance of the promissory note and the terms of the borrowing arrangement.
    <br>• Private Placement Memorandum (PPM) or Offering Memorandum - A document providing investors with detailed information about the business, the risks involved, the terms of the loan, and the business’s financial health, especially for private offerings.
    <br>• Securities Filings (if applicable) - Form D (for Regulation D offerings) filed with the SEC, if the promissory note is offered to accredited investors under exemptions like Rule 506(b) or Rule 506(c).
    <br>• Financial Statements - Balance Sheet and Income Statement to provide a snapshot of the business’s financial health and its ability to repay the loan.
    <br>• Tax Returns - Business Tax Returns (typically 2-3 years) to demonstrate financial stability and the business’s ability to generate income.
    <br>• Disclosure Document (if applicable) - A disclosure document that details the risks and terms associated with the loan, especially if the promissory note qualifies as a security.
    <br>• Loan Agreement or Term Sheet - A high-level document outlining the key terms of the loan (interest rate, repayment structure, etc.) before the formal promissory note agreement.
    <br>• Collateral Documentation (if applicable) - Documentation for any assets pledged as collateral (e.g., real estate titles, equipment appraisals).
    <br>• Investor Verification Documents - For offerings under Regulation D, documents verifying that investors meet the qualifications of accredited investors (e.g., income or net worth documentation).
    <br>• Legal Opinion (if applicable) - A legal opinion letter from an attorney confirming that the promissory note complies with applicable laws and regulations.
    <br>• State or Local Filings (if required) - Any necessary filings or registrations with state or local authorities, particularly for securities offerings or secured loans.
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privatedebtpromisorynotefaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Debt<br>
    Capital Type: Promissory Note</center></p>                        
    <p><center><u><b>Frequently Asked Question for Promissory Note</u></b></center></p>
    <p><u><b>1. What is a Private Debt Promissory Note?</u></b><br>
    • Answer: A Private Debt Promissory Note is a written, legally binding agreement where a company borrows funds from an investor or lender, agreeing to repay the principal amount with interest over a specified period. Unlike public debt, it's a private agreement between the company and the lender.</p>
                             
    <p><u><b>2. Why should I choose a Promissory Note over other funding options like equity or venture capital?</u></b><br>
    • Answer: Promissory notes offer several advantages, such as:
    <br>- Preserving ownership: Unlike equity funding, where investors take an ownership stake, promissory notes do not dilute your control of the company.
    <br>- Fixed repayment terms: You agree to a set repayment schedule, which helps in budgeting and forecasting.
    <br>- Faster and less complex: Compared to equity or venture capital deals, promissory notes are often faster to arrange and simpler in terms of legal documentation.
    <br>- Lower cost of capital (potentially): Interest rates on promissory notes may be lower than those found in equity-based financing, especially for companies with strong credit or proven business models.</p>
                             
    <p><u><b>3. What are the typical terms and conditions of a Private Debt Promissory Note?</u></b><br>
    • Answer: Common terms include:
    <br>- Interest rate: Fixed or variable rate depending on the agreement.
    <br>- Maturity date: The date by which the debt must be repaid, often ranging from 1 to 5 years.
    <br>- Repayment schedule: May include monthly, quarterly, or lump-sum payments.
    <br>- Collateral: Some promissory notes are secured, meaning the lender has a claim on certain assets in case of default.
    <br>- Covenants: Specific conditions the company must meet, such as maintaining certain financial ratios.</p>
                             
    <p><u><b>4. What are the key benefits of using a Promissory Note for raising capital?</u></b><br>
    • Answer:     
    <br>- Speed and Simplicity: The process of structuring and closing a promissory note can be faster than equity financing.
    <br>- Flexibility: Promissory notes can be tailored to suit your business’s needs, such as offering flexible repayment options or different interest structures.
    <br>- Less Dilution of Ownership: Since it’s debt, you won’t lose equity in your business, unlike equity or convertible note financing.
    <br>- Potentially Lower Costs: For businesses with strong credit, the interest rate on promissory notes may be more favorable than the terms for equity investors.</p>
                             
    <p><u><b>5. Are there any risks or drawbacks to using a Private Debt Promissory Note?</u></b><br>
    • Answer:     
    <br>- Obligation to Repay: Even if the business struggles or doesn’t perform well, you are still required to repay the loan with interest. This creates a financial burden, especially for startups or companies with unstable cash flow.
    <br>- No Upside for Lenders: Lenders receive only the agreed-upon interest payments and principal back, regardless of how well the business performs. This could make promissory notes less attractive for investors seeking equity-like returns.
    <br>- Impact on Cash Flow: Regular debt repayments can strain cash flow, especially for businesses with uncertain or seasonal income.
    <br>- Default Risks: If you miss a payment or violate any terms, you may face penalties, accelerated repayment, or legal actions.</p>
                             
    <p><u><b>6. How do interest rates on Promissory Notes compare to other financing options?</u></b><br>
    • Answer: Interest rates for promissory notes are typically fixed and could be lower than equity financing (which requires giving up ownership) or higher-risk debt options, like venture debt. The rate largely depends on your company’s creditworthiness and the nature of the agreement (secured vs. unsecured).</p>
                             
    <p><u><b>7. What’s the difference between a secured and unsecured Promissory Note?</u></b><br>
    • Answer:     
    <br>- Secured Promissory Note: The lender’s investment is backed by company assets (like real estate, equipment, or intellectual property). In the event of default, the lender can claim these assets.
    <br>- Unsecured Promissory Note: No collateral is pledged, meaning the lender relies entirely on the company’s ability to repay the debt. Unsecured notes may carry higher interest rates due to the increased risk for the lender.</p>
                             
    <p><u><b>8. Can the terms of a Promissory Note be adjusted after signing?</u></b><br>
    • Answer: Generally, once the note is signed, the terms are fixed. However, modifications can occur if both parties agree to renegotiate certain aspects of the deal. This may include adjusting the repayment schedule or refinancing the debt.</p>
                             
    <p><u><b>9. What happens if my company defaults on a Promissory Note?</u></b><br>
    • Answer: Defaulting on a promissory note can have serious consequences, including:
    <br>- Acceleration of the debt, requiring you to pay the full amount immediately.
    <br>- Loss of collateral if the note is secured.
    <br>- Potential legal action by the lender to recover funds.
    <br>- Damage to your company’s credit rating, making it harder to obtain future financing.</p>
                             
    <p><u><b>10. What types of businesses should consider using Promissory Notes to raise capital?</u></b><br>
    • Answer: Promissory notes are ideal for businesses that:
    <br>- Need short- to medium-term funding for expansion, equipment, or working capital.
    <br>- Prefer to avoid diluting ownership or giving up equity.
    <br>- Have stable or predictable cash flow and can comfortably meet the repayment terms.
    <br>- Are seeking a relatively straightforward financing option without the complexity of venture capital deals.</p>
                             
    <p><u><b>11. How can I attract investors to buy my Promissory Notes?</u></b><br>
    • Answer: You can attract investors by offering:
    <br>- A competitive interest rate based on current market conditions and your company’s financial health.
    <br>- Attractive repayment terms that align with your business’s cash flow.
    <br>- Strong security or collateral for secured notes, which reduces the lender’s risk.
    <br>- Clear and transparent business performance metrics to instill confidence in your ability to repay the debt.</p>
                             
    <p><u><b>12. Can a Promissory Note be converted into equity?</u></b><br>
    • Answer: Some promissory notes can be structured with a conversion option (often called a convertible promissory note), allowing the lender to convert the debt into equity at a later stage, usually when certain conditions are met, such as a future funding round.</p> 
                             
    <p><u><b>13. What are the tax implications of issuing a Promissory Note?</u></b><br>
    • Answer: The interest paid on a promissory note is generally tax-deductible for the company, which can help reduce taxable income. However, the company must ensure it complies with applicable tax regulations related to interest rates and the terms of the note. From the lender’s perspective, the interest earned is usually taxable as income.</p>

    <p><u><b>14. Can a Private Debt Promissory Note be used in conjunction with other financing methods?</u></b><br>
    • Answer: Yes, companies can use promissory notes in combination with other financing sources, such as equity financing, grants, or other forms of debt. However, it’s important to manage the total debt load to avoid overleveraging the business.</p>
    
    <p><u><b>15. What should be included in the legal agreement of a Promissory Note?</u></b><br>
    • Answer: Key components of the agreement should include:
    <br>- The principal amount of the loan.
    <br>- The interest rate and how it’s calculated.
    <br>- The maturity date and repayment schedule.
    <br>- Collateral (if any).
    <br>- Default provisions and penalties.
    <br>- Warranties and representations by both parties.</p>
    
    <p><u><b>16. Is a promissory note legally binding?</u></b><br>
    • Answer: Yes, a properly executed promissory note is legally binding. As long as the note contains all necessary elements, is signed by the involved parties, and complies with applicable laws, it’s enforceable in court if the borrower defaults or fails to meet their obligations.</p>
    
    <p><u><b>17. Can a promissory note be transferred or sold?</u></b><br>
    • Answer: Yes, a lender may sell or transfer a promissory note to a debt collector if the borrower defaults. Some businesses might purchase promissory notes as well, but this is more common in institutional or corporate investments with high regulatory oversight.</p>
    
    <p><u><b>18. Can you write your own promissory note?</u></b><br>
    • Answer: Yes, you can write your own promissory note. However, it’s advisable to consult an attorney to ensure the legal document is valid and legally enforceable. It’s also a good idea to get your promissory note notarized to prevent future disputes.</p>
    
    <p><u><b>19. Who owns a promissory note? </u></b><br>
    • Answer: The lender—known as the payee—is typically the owner of the original promissory note until the borrower repays the loan. In some cases (like for a mortgage loan), the note may also be held by a financial institution or investment group.</p>                         
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privatedebtpromisorynotetwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR</b></u><br>
    Promissory Note</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    A growth or expansion stage business with consistent revenue, a stable cash flow, and a desire to avoid equity dilution are the ideal candidates for using a Private Debt Promissory Note but promissory notes can be used at any stage of development. 
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    LCs and Corporations (C-Corp and S-Corp) are the most common and ideal entity types for businesses seeking to issue promissory notes. These entities offer limited liability, structured governance, and the ability to raise capital without equity dilution.
    <br>LPs and LLPs can also use promissory notes, but general partners in an LP may bear personal liability for the debt.
    <br>Sole Proprietorships are generally less ideal due to the lack of liability protection, though they can technically issue a promissory note if needed.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    It is completely normal for a business to have raised pre-capital before using a Promissory Note. In fact, having initial capital can position the company more favorably for debt financing, as it demonstrates that the company has already taken steps to build a viable business model.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    While there are no blanket restrictions preventing a company from using a Promissory Note after raising pre-capital, how the pre-capital was raised and the company’s overall financial position could influence its ability to obtain favorable terms or even secure the loan. It is important for the company to carefully consider its existing obligations, investor agreements, and financial health when pursuing debt financing.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    The amount a company can raise using a Promissory Note can vary widely depending on several factors, including the company's financial health, the type of note (secured or unsecured), the lender’s appetite for risk, and the stage of the business. For startups and smaller companies, the range might be between $50,000 to $2 million for unsecured notes, while larger and more established companies could raise anywhere from $500,000 to tens of millions of dollars, especially with secured notes or favorable terms.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    The ideal capital round for a company that wants to use a Promissory Note is typically at the growth stage (such as Series B or Series C), when the company has established revenue, a proven business model, and the ability to manage debt repayments. However, companies in early stages with steady revenue growth or those in later stages preparing for IPOs or acquisitions can also leverage promissory notes, depending on their financial health and the intended use of the capital.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Using multiple tranches to raise capital via a Promissory Note is a viable option and can offer flexibility for companies that need to raise significant amounts of capital over time or wish to align debt with their growth trajectory. Each tranche can be tailored with specific terms, interest rates, and performance milestones, allowing companies to secure capital in stages as they meet their business objectives.

    <br><br>Using a single tranche for a Promissory Note is a common, practical, and straightforward method for raising capital. It is particularly beneficial for businesses that need a lump sum of funding for a specific purpose, have predictable cash flows, and do not need capital in stages.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A Promissory Note provides a business with flexible and direct access to capital, which can be used for a wide variety of purposes, including expanding operations, developing new products, purchasing assets, refinancing debt, or even covering short-term operational expenses.</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Businesses looking to use a Promissory Note need to have moderate to high risk tolerance. This is because taking on debt involves significant financial commitment, and the business must be prepared for potential fluctuations in cash flow, interest rates, and market conditions.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    For a business to use a Promissory Note, it should have a low to moderate capital cost tolerance, depending on its stage of development, financial health, and growth ambitions. This means the company needs to have the ability to manage both direct costs (interest payments and principal repayment) and indirect costs (potential opportunity costs, restrictions, or covenants) associated with debt.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    On average, companies should expect to spend anywhere from $1,000 to $10,000 in upfront costs when raising capital through a Private Debt Promissory Note, depending on the size and complexity of the loan. It’s important for businesses to budget for these costs when considering a private debt option, as they can be a significant part of the financing process.</p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    For a Promissory Note, the timeline for securing capital generally ranges from 3 to 6 weeks, with some deals closing more quickly if the company is well-prepared and the loan is straightforward. However, businesses should be aware that the timeline can be longer for more complex deals, particularly those involving larger loans, intricate terms, or the need for third-party evaluations. To expedite the process, ensuring all documentation is in place and working with an experienced lender can help reduce delays.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)