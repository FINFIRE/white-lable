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


def privateequitysecuritiessimpleagreementfutureequity(request):
    introduction = mark_safe("""
    <p><center><u><b>Capital Market Type: Private Equity Securities</b></u><br>
    Capital Type: Simple Agreement for Future Equity SAFE</center></p>
                             
    <p><b><u>Introduction</u></b><br>
    According to Carta, companies on their cap table platform have signed 101,865 SAFEs since
    2020, which is $14.5 billion invested in early <a href="https://carta.com/data/state-of-pre-seed-q1-2024/">startups</a> Investment amount can vary widely
    depending on the stage of the startup and the investor with some situations seeing significantly
    higher investments depending on the investor's strategy and the company's potential.</p>
                             
    <p><b><u>Definition of Capital Type</u></b><br>                             
    1)A Simple Agreement for Future Equity (SAFE) is an agreement between a company and an
    investor in which the company promises to give the investor a future ownership interest in the
    company if certain triggering events occur, such as a future equity financing or an acquisition of
    the company. The owner of the SAFE does not have an ownership interest in the company unless
    the triggering event occurs and converts the instrument into equity. Like convertible notes,
    SAFEs are often used during seed rounds; however, unlike a convertible note, a SAFE generally
    does not include a valuation of the equity at the time of issuance, deferring that calculation until
    the triggering event occurs. (SEC, 2024)</p>
                             
    <p>2)Simple Agreement for Future Equity (SAFE) “is an agreement between an investor and a
    company that provides rights to the investor for future equity in the company similar to a
    warrant, except without determining a specific price per share at the time of the initial
    investment. The SAFE investor receives the futures shares when a priced round of investment or
    liquidation event occurs. (Levy, n.d.)</p>
                             
    <p>3)A SAFE is an investment contract between a startup and an investor that gives the investor the
    right to receive equity of the company on certain triggering events, such as a: 1) future equity
    financing (known as a next equity financing or qualified financing), usually led by an
    institutional venture capital (VC) fund; and 2) Sale of the company: the price of the equity that
    the SAFE holders receive on conversion is lower than the price of the securities issued to VC
    investors in connection with a next equity financing, based on either a: discount rate or valuation
    cap. (Business Capital 101, 2021)</p>
                             
    <p>4)SAFEs lack the debt hallmarks of convertible notes. In particular, a SAFE has no:
    • Maturity date. Until a conversion event occurs, SAFEs remain outstanding indefinitely.
    • Accruing interest. Investors receive only a right to convert their SAFEs into equity at a
    lower price than the investors in the subsequent financing (based either on the discount or
    valuation cap in their SAFEs). (Simple Agreement for Future Equity (SAFE), n.d.)</p>
    
    <p><b><u>References</u></b><br>
    (2021). In T. D. Smith, Business Capital 101 (p. 32). San Francisco: Imaginary Press.</p>
    
    <p>Levy, C. (n.d.). Safe Financing Documents. Retrieved from Y Combinator
    <a href="https://www.ycombinator.com/documents">https://www.ycombinator.com/documents</a></p>
                             
    <p>SEC. (2024, August 30). Common Startup Securities. Retrieved from SEC
    <a href="https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/common-
    startup-securities">https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/common-
    startup-securities</a></p>
                             
    <p>Simple Agreement for Future Equity (SAFE). (n.d.). Retrieved from West Law
    <a href = "https://content.next.westlaw.com/practical-law/document/Ieffabef3bd2f11e9adfea82903531a62/Simple-Agreement-for-Future-Equity-
    SAFE">https://content.next.westlaw.com/practical-
    law/document/Ieffabef3bd2f11e9adfea82903531a62/Simple-Agreement-for-Future-Equity-
    SAFE</a></p>
    
    <p><b><u>Legal Qualification Requirements</b></u><br>
    • Be a legal entity, typically a corporation, with the ability to issue equity.
    <br>• A legally compliant SAFE agreement, outlining clear terms of conversion.
    <br>• Comply with securities laws and utilize a private offering exemption (e.g., Regulation D
    or Regulation CF in the U.S.).
    <br>• Ensure investor qualification and verify their status.
    <br>• Obtain proper corporate governance approvals, including Board and potentially
    shareholder approval.
    <br>• Prepare and file necessary securities filings, such as Form D with the SEC and any state
    filings required by Blue Sky Laws.
    <br>• Provide disclosures related to the use of proceeds, risk factors, and terms of the offering.
    <br>• Maintain an accurate capitalization table and assess the potential dilution for existing
    stakeholders.
    <br>• Comply with tax and legal regulations, ensuring proper handling of both company and
    investor obligations.</p>
                             
    <p><u><b>Required Supporting Documents</u></b>
    <br>• The SAFE Agreement.
    <br>• Corporate governance documents (e.g., board resolutions) are recommended.
    <br>• Updated Capitalization Table
    <br>• Offering documents like a Private Placement Memorandum (PPM), if applicable.
    <br>• Securities filings and compliance documents (Form D, state filings, etc.).
    <br>• Company formation and organizational documents.
    <br>• Tax and accounting considerations.
    <br>• Investor communication materials.</p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiessimpleagreementfutureequityfaq(request):
    introduction = mark_safe("""
        <p><h1><center><u><b>Frequently Asked Question for Simple Agreement for Future Equity</u></b></center></h1></p>
    <p><u><b>1. What is a SAFE, and how does it work?</u></b><br>
    • Answer: A SAFE (Simple Agreement for Future Equity) is an agreement used by startups
    to raise capital without setting a current valuation. Investors provide capital in exchange
    for the right to convert into equity during future financing or liquidity events (e.g.,
    acquisition, IPO), typically with a discount or valuation cap.</p>
                             
    <p><u><b>2. What are the key advantages of using a SAFE compared to other fundraising options?</u></b><br>
    • Answer: SAFEs offer several benefits, including:
    <br>Simplicity: Easy to negotiate with fewer terms and less legal complexity.
    No Interest or Maturity: Unlike convertible notes, SAFEs do not accrue interest or have a
    maturity date.  
    <br>Flexible Valuation: Delays setting a valuation, beneficial for early-stage startups.
    <br>Low Transaction Costs: Generally lower legal and administrative costs.</p>
                             
    <p><u><b>3. Why should my company choose a SAFE over a convertible note?</u></b><br>
    • Answer: SAFEs are often preferred because:
    No Debt Structure: SAFEs are not debt, so no interest or maturity pressure like convertible
    notes.
    <br>Simplicity: Fewer negotiation points and no interest rates or maturity dates.
    Less Risk of Dilution: No interest component means less dilution compared to convertible
    notes.</p>
                             
    <p><u><b>4. How does the valuation cap or discount work in a SAFE?</u></b><br>
    • Answer: The valuation cap and discount are key terms:
    Valuation Cap: Sets a maximum valuation for conversion, ensuring favorable equity terms
    for investors.
    <br>Discount: Provides investors with a discounted share price at conversion, ensuring they
    receive equity at a lower price than later investors.</p>
                             
    <p><u><b>5. What are the risks associated with using SAFEs for fundraising?</u></b><br>
    •Answer:<br>
    Dilution: Future investors may face dilution when SAFEs convert into equity.
    No Immediate Control: SAFE investors don’t have voting rights or a guaranteed return
    until conversion.

    <br>Triggering Events: No guaranteed triggering event for conversion, potentially leaving
    investors without liquidity for a long time.</p>
                             
    <p><u><b>6. What types of companies are best suited for using SAFEs?</u></b><br>
    • Answer: SAFEs are ideal for early-stage startups that:
    <br>Need capital quickly.
    <br>Don’t have a clear valuation.
    <br>Want to avoid the complexity of debt instruments like convertible notes.
    <br>Are seeking funding from investors familiar with SAFEs</p>
    
    <p><b><u>7. Can SAFEs be used for equity crowdfunding?</b></u>
    <br>• Answer: Yes, SAFEs can be used in equity crowdfunding under Regulation CF, where
    terms such as the valuation cap and discount are disclosed to all potential investors.</p>
                             
    <p><b><u>8. How long does it take to raise capital using SAFEs?</b></u><br>
    • Answer: SAFEs can be raised quickly, typically taking a few weeks to a few months, due
    to their simpler legal and administrative processes compared to traditional equity rounds.</p>
                             
    <p><b><u>9. How does the SAFE convert into equity?</b></u>
    <br>• Answer: SAFEs convert when a triggering event occurs, such as:
    <br>A subsequent equity financing round.
    <br>An acquisition or liquidity event.
    <br>An IPO. Conversion occurs at a price per share based on the valuation cap or discount.</p>
                             
    <p><b><u>10. Are SAFEs legally binding and enforceable?</b></u><br>
    • Yes, SAFEs are legally binding contracts, and both the company and investor must abide
    by the conversion terms once a triggering event happens.</p>
                             
    <p><b><u>11. How does a SAFE affect the company’s cap table?</b></u>
    <br>• Answer: SAFEs don’t affect the cap table until they convert into equity. Once converted,
    they dilute ownership percentages based on the terms of the SAFE.</p>
                             
    <p><b><u>12. Can SAFEs be negotiated, or are they standard agreements?</b></u>
    </br>• Answer: SAFEs can be negotiated on terms such as the valuation cap and discount,
    depending on the investor and the capital being raised, though they are often standardized
    for simplicity.</p>
                             
    <p><b><u>13. What happens if my company is acquired before the SAFE converts?<br></b></u>
    • Answer: If an acquisition occurs before the SAFE converts, it typically converts into equity
    or is repaid based on the SAFE’s terms, with investors potentially receiving a portion of
    the acquisition proceeds.</p>
                             
    <p><b><u>14. Do SAFEs work for international companies?</b></u>
    <br>• Answer: SAFEs can work for international companies, but the terms must comply with
    local securities laws, and the SAFE may need to be adjusted to fit the legal requirements
    of the country in which the company is incorporated.</p>
                             
    <p><b><u>15. How do SAFEs affect future fundraising rounds?</b></u><br>
    • Answer: SAFEs affect future rounds by:
    <br>Dilution: SAFEs dilute existing shareholders when they convert into equity.
    <br>Cap Table Complexity: The cap table becomes more complex, which may affect
    negotiations in future rounds.                                 
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiessimpleagreementfutureequitytwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    introduction = """
    <p><center><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Simple Agreement for Future Equity (SAFE)</p></center>
    
    <p><b><u>1- Stage of Development Assessment</b></u><br>
    While {n} is in the {stage} stage, utilizing a Simple Agreement for Future Equity
    (SAFE) offers several key benefits for raising capital. A SAFE allows you to raise funds without
    <u>immediately</u> diluting ownership, as it converts into equity at a later financing round, typically at
    a discount or with a valuation cap. This flexibility is ideal for a growing company that wants to
    quickly secure capital while deferring valuation decisions to a future funding round when more
    data and growth potential are clearer.<br>
    With a SAFE, you can raise capital without immediately setting a valuation for your company,
    which allows for greater flexibility in the early stages of growth.</p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Utilizing a Simple Agreement for Future Equity (SAFE) for a {entity} offers several
    advantages. With a SAFE, you can raise capital without immediately setting a valuation for your
    company, which allows for greater flexibility in the early stages of growth. Investors provide
    funding in exchange for the promise of equity in a future financing round, typically with
    favorable terms such as a discount or valuation cap.(because a corporation has shares that require a valuation cap table).</p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    {n} has already raised {preraise} in pre-capital, utilizing a Simple Agreement for
    Future Equity (SAFE) enables the company to attract a wide range of investors, including those
    who may be looking for a more straightforward and less risky entry point into the business. With
    a SAFE, Dining Empire can raise funds quickly and efficiently, which is crucial for scaling
    operations, expanding product offerings, and strengthening its market presence.</p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    Because {n} has already raised {preraise} through a {premarket}, utilizing a Simple
    Agreement for Future Equity (SAFE), continuing to use a SAFE in future capital rounds can be
    beneficial for both the company and its investors, helping to streamline fundraising, align
    expectations, and reduce complexity. SAFEs also streamline the fundraising process, as they are
    simpler and faster to execute compared to traditional equity rounds, with fewer legal
    complexities and lower transaction costs.</p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Using a SAFE to raise {raisegoal} offers simplicity, flexibility, and speed, all of which are critical
    when you are focusing on scaling a growing business. The ability to defer valuation while still
    raising the necessary funds makes it a highly efficient tool for {n}.</p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Using a SAFE in the {rounds} will allow {n} to raise capital quickly and
    efficiently, while keeping things simple, retaining control, and avoiding the complexities of
    immediate valuation and equity dilution. It offers a flexible and investor-friendly solution that
    supports early-stage growth.</p>
    
    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Using a SAFE for {tranch} tranches of capital allows the company to raise funds flexibly, efficiently,
    and without the need for early-stage valuation negotiations, which can be particularly beneficial
    as Dining Empire scales and grows.</p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    A SAFE provides a flexible, efficient, and cost-effective way to raise capital for a variety of
    business needs, especially in the early stages of growth. It offers the ability to address critical
    financial needs while keeping the company on track for future growth and success. SAFE allows
    you to raise capital for a wide range of purposes, including:<b>note(should be used from this list: {useoffund})</b>
    <br>1. Startup – Working Capital - note should be updated from the list
    <br>2. Growth Scalability - note should be updated from the list
    <br>3. Marketing & Sales - note should be updated from the list
    <br>4. Cash Flow Capital - note should be updated from the list
    <br>5. Human Capital - note should be updated from the list
    <br>6. Other - note should be updated from the list
    </p>

    <p><b><u>9 - Risk Assessment</b></u><br>
    A Simple Agreement for Future Equity (SAFE) is an excellent option for a company that is
    comfortable with high risk and seeking to attract investors who are looking for high returns and
    are interested in supporting early-stage, high-growth companies. SAFEs align well with {n} objectives by offering a straightforward, flexible approach to raising capital.
    </p>
    
    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The principal's willingness to accept higher capital costs can benefit the company when using a
    Simple Agreement for Future Equity (SAFE), particularly if the company is seeking rapid
    growth.</p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    With a {upfrontcost} budget, a SAFE could be a cost-effective option for raising early-stage
    capital, especially if you are looking to avoid the complexities and higher costs of more
    traditional equity rounds or venture capital. However, if you're planning to raise a larger amount
    of capital or need immediate equity dilution, other funding options might be more appropriate.
    SAFEs work well for smaller, early-stage capital needs, and if you are comfortable with the risk,
    they can be a good way to secure funding with a low upfront cost.</p>
    
    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    In general, a SAFE is designed to be a fast way for early-stage companies to raise capital without
    the complexities of equity rounds or venture capital, so {n} should be able to get
    capital in less than two months on average.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)