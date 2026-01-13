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
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Convertible Note</p>
    <p><b><u>Introduction</u></b><br>
    Issuance of convertible securities for the first half of 2024 has been particularly strong with
    approximately $40 billion of new issuance coming to the market. <a href="https://www.newyorklifeinvestments.com/insights/2024-outlooks/mackay-converts-3q-2024-outlook
    ">Our expectation is that
    issuance will meet or exceed $80 billion this year which compares to $53.4 billion of new
    issuance in 2023 and $28.7 billion of new issuance in 2023</a>. According to the Angel Capital
    Association’s 2020 Angel Funders Report, <a href="https://www.angellist.com/learn/convertible-note">37% of angel deals were done using convertible
    notes.</a> From a representative sample of worldwide startups, it seems that convertible notes are
    used <a href="https://www.equidam.com/discount-rate-for-a-convertible-note">33.02% of the times for seed funding and 62.53% for bridge financing.</a>
    </p>
                             
    <p><b><u>Definition of Capital Type</u></b><br>
    1) A convertible note is a debt security that allows the holder to convert the principal and accrued
    interest into shares of the issuer’s common stock, subject to certain terms, including a conversion
    price determined by a discount to the price per share in the issuer’s next financing round, or at a
    valuation cap. The note may be repaid in cash at maturity if conversion does not occur, or it may
    convert into equity upon the occurrence of certain triggering events, such as a qualified financing
    or acquisition. (Alerasoul, n.d.)</p>
                             
    <p>2) A convertible note is “a debt instrument often used by angel or seed investors looking to fund
    an early-stage startup that has not been valued explicitly. After more information becomes
    available to establish a reasonable value for the company, convertible note investors can convert
    the note into equity. The firm valuation will usually be determined during the Series A financing
    round. So instead of a return in the form of principal plus interest, the investor would receive
    equity in the company.” This document allows the investors to either be in equity (stock) or debt
    and gives them the ability to choose either or. A convertible note usually starts as debt
    (promissory note) and after a time converts. It should include a discount and yield. Principal
    and interest can be converted into equity.
    (Smith, 2021)</p>
                             
    <p>3) A convertible note is a short-term debt agreement that converts into equity at a future date.
    Usually, this happens when one of these events takes place:
    <br>• The company raises enough capital to reach a pre-determined benchmark.
    <br>• The term of the loan expires.
    <br>• The company is sold.
    <br>These notes enable a company to raise capital without making an explicit public valuation. In the
    agreement, the parties make their own estimate of the company’s value. This gives the company
    and the investor more flexibility to set their own terms for repayment and conversion.
    Companies that issue convertible notes benefit from reduced cash interest payments on their
    business loans. Additionally, when the note converts, the debt is retired.
    Convertible notes are popular with smaller companies and familiar to many investors. They are
    simple and inexpensive. However, they can lead to unintended outcomes and uncertainty about
    future control and company ownership. Consult a lawyer as you negotiate any convertible debt
    financing. (Convertible Notes Overview)</p>
                             
    <p>4) Convertible notes are structured as loans to convert them to an equity stake in the company in
    the future. As far as the process of funding is concerned, the debt is automatically converted to a
    known amount of equity shares (common or preferred) at the time of closing the Series A
    financing round.<br>
    To put it simply, after investors initially loaned capital to a new company (startup) and it’s grown
    enough to repay the debt, investors wish to get a predetermined amount of preferred stock
    instead of receiving their money with interest. It is part of the startup’s original preferred stock
    financing based on the terms of the convertible note. (Team)</p>
    
    <p><b><u>References</b></u><br>
    Alerasoul, A. (n.d.). Understanding Convertible Debt Valuation. Retrieved from Valuation<br>
    Research: <a href="https://www.valuationresearch.com/insights/understanding-convertible-debt-valuation/">https://www.valuationresearch.com/insights/understanding-convertible-debt-valuation/</a></p>
                             
    <p>Convertible Notes Overview. (n.d.). Retrieved from Penn Law School:<br>
    <a href="https://www.law.upenn.edu/clinic/entrepreneurship/startupkit/convertible-note.pdf">https://www.law.upenn.edu/clinic/entrepreneurship/startupkit/convertible-note.pdf</a></p>
                             
    <p>Smith, T. D. (2021). Business Capital 101. Imaginary Press.</p>
                             
    <p>Team, C. (n.d.). Convertible note. Retrieved from Corporate Finance Institute:<br>
    <a href="https://corporatefinanceinstitute.com/resources/fixed-income/convertible-note/">https://corporatefinanceinstitute.com/resources/fixed-income/convertible-note/</a></p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Business Entity: The company must be a legally registered business entity, typically a
    corporation (C-Corp or S-Corp) or limited liability company (LLC).
    <br>• Securities Laws Compliance: The company must comply with U.S. securities laws,
    particularly regarding exemptions for private offerings (e.g., Regulation D, Regulation A,
    Regulation Crowdfunding (Reg CF)).
    <br>• Investor Accreditation (if using Regulation D):
    <br>• If using Regulation D (e.g., Rule 506(b) or 506(c)), investors must either be accredited
    investors or, in some cases, a limited number of non-accredited investors.
    <br>• Private Placement Memorandum (PPM): While not mandatory, the company should
    provide a PPM outlining the terms, risks, and business details, especially for Reg D offerings.
    <br>• Anti-Fraud Compliance: The company must avoid misstatements or omissions of
    material information to investors
    <br>• Investor Suitability: The company must ensure that investors understand the risks
    associated with the convertible note and that the offering is suitable for the investor’s financial
    situation (particularly under Reg D).
    <br>• State Securities Compliance (Blue Sky Laws): The company must ensure compliance
    with state securities laws (blue sky laws), which may require filing notices or obtaining
    exemptions in states where investors reside.
    <br>• Convertible Note Agreement must be in place and include: principal amount, interest rate,
    maturity date, conversion terms, valuation cap, and discount rate (if applicable).
    <br>• Board and Shareholder Approvals: Depending on the company’s governance structure,
    board of directors and/or shareholder approval may be required before issuing convertible notes.
    <br>• Proper Use of Funds: The funds raised through convertible notes must be used for lawful
    purposes and consistent with the business plan and investor expectations disclosed in offering
    documents.
    <br>• Form D Filing (if applicable): If raising capital under Regulation D, the company must
    file Form D with the SEC within 15 days of the first sale of securities.
    <br>• Tax Compliance: The company must ensure that it complies with applicable tax laws,
    including any tax implications of issuing convertible notes and potential conversion into equity.</p>
                             
    <p><b><u>Supporting Document List</b></u>
    <br>• Convertible Note Agreement
    <br>• Private Placement Memorandum (PPM) (Optional but Recommended)
    <br>• Investor Accreditation Verification (If Applicable)
    <br>• Form D Filing (If Applicable)
    <br>• State Securities Filings (Blue Sky Filings)
    <br>• Cap Table (Capitalization Table)
    <br>• Board Resolution or Shareholder Approval (If Required)
    <br>• Financial Statements
    <br>• Use of Proceeds Statement
    <br>• Investor Subscription Agreement
    <br>• Risk Disclosures                                                                          
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesconvertiblenotefaq(request):
    introduction = mark_safe("""                 
    <p><u><b>Frequently Asked Question for Convertible Notes</u></b></p>
                             
    <p><u><b>1. What is a Convertible Note?</u></b><br>
    •Answer: A Convertible Note is a short-term debt instrument that converts into equity,
    typically at a later funding round. The company borrows money from investors and
    agrees to convert the debt into equity when a predetermined event, like a future financing
    round, occurs.</p>
                             
    <p><u><b>2. Why should I choose a Convertible Note over other funding options?</u></b><br>
    • Answer: 
    <br>-Speed and simplicity: Convertible notes are quicker to issue compared to equity
    rounds or other types of financing, as they don’t require complex valuation negotiations.
    <br>-Cost-effective: Legal and administrative costs are often lower than for equity funding
    rounds, making it a more affordable option for early-stage companies.
    <br>-Deferred valuation: Convertible notes delay the need to determine the company’s
    valuation until a later financing round, which can be beneficial if the business is still early
    and hard to value.
    </p>
                             
    <p><u><b>3. What are the key terms of a Convertible Note?</u></b><br>
    • Answer: The key terms typically include:
    <br>- Principal amount (the loan amount)
    <br>-Interest rate (the amount the note accrues over time)
    <br>- Maturity date (the date the note becomes due, unless converted)
    <br>-Conversion terms (how the loan will convert into equity, including the discount rate
    and/or valuation cap)
    </p>
                             
    <p><u><b>4. How does the conversion process work?</u></b><br>
    • Answer: When the company raises a future round of funding (often referred to as a
    "qualified financing round"), the convertible note converts into equity at a discounted
    price or based on a valuation cap. The discount and valuation cap provide early investors
    with a better price per share than new investors in the subsequent round.</p>
                             
    <p><u><b>5. What is a Valuation Cap and a Discount Rate?</u></b><br>
    • Answer: 
    <br>-Valuation cap: The maximum company valuation at which the convertible note
    will convert into equity, providing early investors with protection from excessive dilution
    if the company’s valuation grows rapidly.
    <br>-Discount rate: A percentage discount on the price per share paid by new investors in a
    future funding round. This gives note holders a better price compared to new investors.</p>
                             
    <p><u><b>6. What happens if the company doesn't raise a future funding round?</u></b><br>
    • Answer:  If the company does not raise a future round of funding before the note matures,
    the company typically has to repay the principal amount along with any accrued interest.
    In some cases, the note may convert into equity at the discretion of the investor or under
    agreed-upon terms if other events occur.</p>
                             
    <p><u><b>7. Can a Convertible Note be used to raise capital from non-accredited investors?</u></b><br>
    • Answer: Generally, Convertible Notes are issued to accredited investors. However, it may
    be possible to raise funds from non-accredited investors through Regulation
    Crowdfunding (Reg CF) or Regulation A offerings, which allow for broader participation,
    subject to regulatory requirements.
    </p>
                             
    <p><u><b>8. What is the typical maturity date for a Convertible Note?</u></b><br>
    • Answer: Maturity dates typically range from 12 to 24 months, though they can be shorter
    or longer depending on the agreement. If the note reaches maturity without converting
    into equity, the company must repay the loan unless another agreement is reached.</p>
                             .
    <p><u><b>9. What are the risks of issuing a Convertible Note?</u></b><br>
    • Answer:
    <br>-Debt obligation: Until converted, the convertible note is a debt, meaning the
    company is obligated to repay the principal and interest if it does not convert.
    <br>-Dilution: Issuing convertible notes can result in significant dilution for existing
    shareholders when the notes convert into equity.
    <br>-Complexity of terms: Negotiating terms like valuation caps, interest rates, and discounts
    can be complicated and may require legal assistance.
    </p>
                             
    <p><u><b>10. How does a Convertible Note impact the company’s ownership structure?</u></b><br>
    • Answer:Since the convertible note converts into equity in the future, it impacts the
    company’s ownership structure by diluting the current shareholders once the note holders
    convert their debt into equity. The exact amount of dilution depends on the note’s terms
    (e.g., discount rate and valuation cap).
    </p>
                             
    <p><u><b>11. What happens if an investor doesn’t want to convert their note into equity?</u></b><br>
    • Answer:  If the investor does not want to convert, they can usually choose to be repaid the
    principal amount along with any accrued interest by the maturity date, unless other terms
    in the agreement dictate otherwise.
    </p>
                             
    <p><u><b>12. What are the tax implications for the company and investors?</u></b><br>
    • Answer: 
    <br>-For the company: The interest paid on convertible notes is generally tax-
    deductible. However, if the note converts into equity, the conversion does not trigger a
    taxable event.
    <br>-For investors: Investors generally do not incur tax on the interest income until it is paid
    out. The conversion into equity is also typically not a taxable event, unless the note is
    deemed to have been paid out in a sale or other event.
    </p>
                             
    <p><u><b>13. How is a Convertible Note different from a traditional loan or equity financing?</u></b><br>
    • Answer:
    <br>-Unlike a traditional loan, a convertible note doesn’t require monthly payments
    or collateral; instead, it’s a debt that converts into equity at a future financing round.
    <br>-Unlike equity financing, convertible notes do not immediately dilute ownership. The
    conversion happens later, allowing the company to delay valuation discussions until a
    larger funding round.
    </p>
                             
    <p><u><b>14. Can a company issue multiple Convertible Notes?</u></b><br>
    • Answer:  Yes, a company can issue multiple convertible notes in different rounds of
    fundraising. However, each note may have different terms (e.g., discount rates, maturity
    dates), which can complicate future conversion or valuations.</p> 
                             
    <p><u><b>15. What should a company consider when structuring a Convertible Note offering?</u></b><br>
    • Answer: The company should consider:
    <br>-Investor incentives: Offering a reasonable discount or valuation cap to attract investors.
    <br>-Company goals: Determining the right timing for conversion and the ideal future
    financing round.
    <br>-Dilution control: Understanding how the notes will impact the ownership structure when
    converted into equity.
    <br>-Legal considerations: Consulting with legal advisors to ensure the terms comply with
    applicable laws and are in the best interests of the company.
    </p>                                                                                                               
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesconvertiblenotetwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    risktolerance = EQuestions8.objects.get(user=request.user).Selected_Option 
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Convertible Note</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    While {n} is in the {stage} stage of business development, utilizing convertible notes provides
    the ability to raise capital without immediately diluting equity allowing founders to retain greater
    control in the early stages. They also provide flexibility to postpone the valuation, which is often
    a challenge for growing businesses, until a later funding round.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Utilizing convertible notes is a good option for {entity}. They are less likely to be
    used for LLCs but it is possible.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    {n} has already raised pre-capital so utilizing convertible notes can provide the ability to
    secure additional funding which is especially valuable as the company continues to grow and
    refine its market position.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Utilizing convertible notes is a natural next step for a company that has already raised pre-capital
    through different market types. The company can attract investors with the potential for future
    equity conversion, often at a discounted rate. This flexibility allows the company to continue
    scaling its operations and expanding its investor base.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Convertible notes offer businesses an efficient way to raise capital with no specific funding
    limits set by law. The amount raised through convertible notes can vary depending on investor
    interest and the terms negotiated, allowing the company to raise the necessary funds without
    being restricted by a set cap. This will allow {n} to hit their goal of raising {raisegoal}.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    While {n} is engaged in the {rounds} of capital raising, using convertible notes allow
    the company to raise funds from a wide range of investors. Convertible notes offer customizable
    terms, such as conversion discounts or valuation caps, which can be tailored to attract investors
    while aligning with the company's growth objectives. Additionally, they offer the opportunity to
    engage investors in the company's success.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Since {n} plans to raise capital in {tranch} tranche/tranches, using convertible notes allow for a
    straightforward, single round of funding. By using convertible notes, the company can streamline
    the process, aligning the fundraising efforts with specific business goals without the complexities
    of setting a valuation upfront or raising funds in multiple stages.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A key benefits of using convertible notes is that there are no strict limitations on how the funds
    can be utilized, providing you with the freedom to allocate capital as needed across various
    aspects of your business. Whether {n} is looking to expand operations, enhance marketing
    strategy, boost sales efforts, or hire top talent, convertible notes allow you to use the funds
    without restrictions. While you'll need to clearly outline the intended use of funds in your
    offering documents to ensure transparency and maintain investor confidence, convertible notes
    offer a versatile and effective solution for:<b>note(should be used from this list: {useoffund})</b>
    <br>1. Growth Scalability
    <br>2. Marketing & Sales
    <br>3. Human Capital
    <br>4. Other
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Convertible notes offer a unique way to raise capital for companies in the growth stage by
    appealing to investors with a {risktolerance}. For investors, the high potential for return
    makes convertible notes an attractive option, especially in high-risk, high-reward investment
    scenarios. This approach helps align the interests of both the company and its investors,
    providing a mutually beneficial path to future growth.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    Convertible notes are one of the {enterprisecost} options to raise capital. A founder with a high capital
    cost tolerance can leverage convertible notes as a strategic tool to raise capital while managing
    the financial uncertainties of early-stage growth. This allows the founder to maintain control over
    the company while providing investors with the potential for future equity at a discounted rate or
    with a valuation cap.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>Convertible notes offer a cost-effective solution for companies looking to raise capital. Unlike
    traditional equity rounds or venture capital, convertible notes can minimize upfront legal and
    administrative expenses, as they do not require an immediate valuation or the complex processes
    associated with equity financing. With convertible notes, the primary costs typically include legal
    fees for drafting the note agreement and filing necessary documents, as well as minimal costs
    related to investor outreach and marketing. These expenses are generally much lower than those
    tied to traditional funding methods such as equity rounds or IPOs, making it a feasible option
    within the {upfrontcost} budget range.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>Convertible notes are an excellent option for companies looking to raise capital within a 
    {upfronttime} timeframe. Since convertible notes do not require an immediate valuation and involve less
    complex legal structures compared to equity financing, they can be executed more quickly. The
    process typically involves drafting the convertible note agreement, negotiating terms with
    investors, and securing legal compliance. By using convertible notes, a company can secure the
    necessary funding while minimizing delays, allowing for faster capital infusion to support
    growth and expansion.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,risktolerance=risktolerance,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)