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


def privateequitysecuritiesregulationd504_(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Rule 504</center></p>
    
    <p><b><u>Introduction</u></b><br>
    Providing quicker and lower-cost access to investor funding, Regulation D is ideal for those who wish to syndicate a business and entrepreneurs who need fast access to cash. The benefits of using Reg D 504 are the streamlined process that doesn’t require ongoing reporting, much lower costs of making the offering, and the ability to sell to accredited and non-accredited investors <a href="https://www.moschettilaw.com/rule-504-of-reg-d/">(source)</a>.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    1) Rule 504 of Regulation D provides an exemption from the registration requirements of the federal securities laws for some companies when they offer and sell up to $10,000,000 of their securities in any 12-month period.  Except in limited circumstances, purchasers of securities offered pursuant to Rule 504 receive "restricted" securities, meaning that the securities cannot be sold for at least six months or a year without registering them. (Smith, 2021)

    <br><br>2) Companies that comply with the requirements of Rule 504 do not have to register their offering of securities with the SEC, but they must file what is known as a "Form D" electronically with the SEC after they first sell their securities. Form D is a brief notice that includes the names and addresses of the company’s promoters, executive officers and directors, and some details about the offering, but contains little other information about the company.  You can access the SEC’s EDGAR database to determine whether the company has filed a Form D. 

    <br><br>Even if a company takes advantage of an exemption from registration, a company should take care to provide sufficient information to investors to avoid violating the antifraud provisions of the securities laws. This means that any information a company provides to investors must be free from false or misleading statements. Similarly, a company should not exclude any information if the omission makes what is provided to investors false or misleading. (Rule 504 of Regulation D, n.d.)

    <br><br>3) Some companies are not eligible for a Rule 504 exemption. These include:
        <br>• Investment companies
        <br>• Exchange Act reporting companies
        <br>• Companies with no specific business plan
        <br>• Companies that plan to engage in a merger or acquisition with an unidentified company or companies
        <br>• Companies that are liable for a "bad actor" disqualification
    <br>(Kenton, 2024)

    <br><br>4) You also need to consider the securities themselves. In most cases, securities sold under Reg D Rule 504 are restricted securities. Bearing a symbol to mark them as restricted, you can only sell these types of securities in a legitimate unregistered transaction. For example, imagine that you’re an investor purchasing unregistered equity securities in a company. If those securities are restricted, you can’t then sell those securities to somebody else in a registered transaction. Instead, you can only sell them in an unregistered transaction completed under the rules of Reg D. (Rule 504 of Reg D – The Former Heavyweight Syndication Champ, n.d.) 
    </p>
                             
    <u><b><p>References</u></b><br>
    Kenton, W. (2024, April 05). SEC Regulation D (Reg D): Definition, Requirements, Advantages. Retrieved from Investopedia: <a href="https://www.investopedia.com/terms/r/regulationd.asp">https://www.investopedia.com/terms/r/regulationd.asp</a>
    <br><br>Rule 504 of Reg D – The Former Heavyweight Syndication Champ. (n.d.). Retrieved from Moschetti Law: <a href="https://www.moschettilaw.com/rule-504-of-reg-d/">https://www.moschettilaw.com/rule-504-of-reg-d/</a>
    <br><br>Rule 504 of Regulation D. (n.d.). Retrieved from Investor.gov: <a href="https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-504-regulation-d">https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-504-regulation-d</a>
    <br><br>Smith, T. D. (2021). Business Capital 101. San Francisco: Imaginary Press.
    </p>
    
    <p><b><u>Legal Qualification Requirements</u></b>
    <br>• Entity Type: Must be a U.S.-based company (corporation, LLC, etc.) that is not publicly traded.
    <br>• Offering Size: Can raise up to $10 million within a 12-month period.
    <br>• Investor Eligibility: Can offer to both accredited and non-accredited investors, but must comply with state laws.
    <br>• General Solicitation: General solicitation is not allowed unless the offering complies with Rule 506(c) (for accredited investors only).
    <br>• State Compliance: Must follow state securities laws (blue sky laws) and may need to register the offering in each state.
    <br>• Resale Restrictions: Securities sold cannot be resold for one year.
    <br>• No Criminal Background: Company management cannot have felony or securities-related misdemeanor convictions.
    <br>• Bad Actor Disqualification: Company and its officers must not be disqualified due to past misconduct.
    <br>• Form D Filing: Must file Form D with the SEC to notify them of the offering.
    </p>
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Form D: Must be filed with the SEC to notify them of the offering.
    <br>• State Filings: Required filings with state securities regulators (blue sky laws) for each state where securities are offered.
    <br>• Private Placement Memorandum (PPM): Optional but recommended to provide detailed disclosures to investors.
    <br>• Investor Questionnaires: Used to verify investor eligibility, especially for accredited investors.
    <br>• Accredited Investor Verification: Needed if using general solicitation (to confirm accredited investor status).
    <br>• Subscription Agreement: A legally binding agreement between the company and investors outlining the terms of the investment.
    <br>• Financial Statements: May be required, typically unaudited, to disclose the company’s financial position.
    <br>• State-Specific Disclosure Forms: Additional forms required by individual states for compliance.
    <br>• Legal Opinion: May be needed in certain cases to confirm compliance with securities laws. 
    </p>
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd504_faq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Equity Securities<br>
    Capital Type: Rule 504</center></p>                        
    <p><center><u><b>Frequently Asked Question for Rule 504</u></b></center></p>
    <p><u><b>1. What is Regulation D Rule 504, and how does it help my company raise capital?</u></b><br>
    • Answer: Regulation D Rule 504 provides an exemption from SEC registration requirements, allowing companies to raise up to $10 million in a 12-month period without the need to register with the SEC. It is ideal for businesses seeking capital from a large number of investors and offers the ability to conduct general solicitation, meaning the company can advertise the offering to the public.</p>
                             
    <p><u><b>2. How much can my company raise under Regulation D Rule 504?</u></b><br>
    • Answer: Your company can raise up to $10 million in a 12-month period under Rule 504. This limit is a significant benefit for businesses that need a substantial amount of capital but do not want to go through the more burdensome SEC registration process for larger offerings.</p>
                             
    <p><u><b>3. What are the key advantages of using Rule 504 over other capital-raising methods?</u></b><br>
    • Answer: Key advantages of Rule 504 include:
    <br>- No SEC Registration: Unlike public offerings, you don’t have to go through the expensive and time-consuming process of registering with the SEC.
    <br>- General Solicitation: You can publicly advertise your offering (via social media, email, or other means), potentially attracting a larger pool of investors.
    <br>- Flexibility in Investor Types: Rule 504 allows you to raise capital from both accredited and non-accredited investors (with certain restrictions), expanding your potential investor base.
    <br>- Simplified Regulatory Compliance: While you need to file Form D with the SEC and comply with state securities laws, the process is less complex than full registration.</p>
                             
    <p><u><b>4. Who can invest in a Rule 504 offering?</u></b><br>
    • Answer: Rule 504 allows you to raise funds from both accredited and non-accredited investors, which is a significant advantage over other SEC exemptions (like Rule 506(b)) that typically limit you to accredited investors only. However, if you accept non-accredited investors, there are limitations on the number of such investors (no more than 35 non-accredited investors) and the company must provide additional disclosures to ensure investor protection.</p>
                             
    <p><u><b>5. Are there any investor restrictions under Rule 504?</u></b><br>
    • Answer: While Rule 504 allows both accredited and non-accredited investors, there are key restrictions:
    <br>- Non-accredited Investors: The number of non-accredited investors cannot exceed 35 in total, and the company must provide adequate financial and business information to these investors.
    <br>- State-Specific Regulations: You need to comply with individual state laws (Blue Sky laws), which might impose additional requirements for investors in certain states.
    </p>
                             
    <p><u><b>6. Can my company advertise or solicit investments publicly under Rule 504?</u></b><br>
    • Answer: Yes, Rule 504 allows general solicitation, meaning your company can publicly advertise its securities offering. You can use various forms of advertising, including social media, online campaigns, or events, to reach a broader pool of investors. However, the advertising must comply with the overall offering requirements, and you must ensure that the offering is conducted in accordance with all applicable laws.</p>
                             
    <p><u><b>7. What are the main legal and compliance requirements for Rule 504?</u></b><br>
    • Answer: The key legal and compliance steps include:
    <br>- Filing Form D: You must file Form D with the SEC within 15 days after the first sale of securities.
    <br>- Blue Sky Filings: You must comply with state-level securities laws, known as Blue Sky laws, which may require additional filings or fees in the states where you are soliciting investors.
    <br>- Disclosure: If accepting non-accredited investors, you must provide sufficient disclosure to ensure that investors are well-informed about the offering.
    <br>- Investor Verification: You may need to verify the status of your investors, particularly if you are soliciting non-accredited individuals.</p>
                             
    <p><u><b>8. What are the key costs associated with using Rule 504 to raise capital?</u></b><br>
    • Answer: The costs of raising capital under Rule 504 generally include:
    <br> Legal Fees: Preparing offering documents, including the Private Placement Memorandum (PPM), and filing Form D. Legal fees can range from $10,000 to $50,000 or more, depending on the complexity of the offering.
    <br> State Filing Fees: Depending on the states involved, you will incur Blue Sky filing fees (ranging from $1,000 to $10,000+).
    <br> Marketing and Solicitation: If you engage in advertising or marketing to attract investors, this can add an additional $5,000 to $30,000 in costs.
    <br> Placement Agent or Broker Fees: If you hire intermediaries, expect fees of 1% to 5% of the total capital raised.</p>
                             
    <p><u><b>9. How long does it take to raise capital using Rule 504?</u></b><br>
    • Answer: The typical timeline to raise capital under Rule 504 ranges from 6 to 12 weeks. This timeline includes time for:
    <br>- Document preparation (legal documents, PPM, and filings),
    <br>- Investor solicitation and commitments,
    <br>- Filing Form D and completing state filings.
    <br>- The time can be shorter if your company is well-prepared and has a strong marketing and solicitation strategy, or longer if the offering is more complex.</p>
                             
    <p><u><b>10. What types of businesses can use Regulation D Rule 504?</u></b><br>
    • Answer: Rule 504 is available to most private companies, including startups, growth-stage businesses, and small to mid-sized companies. However, it is not available to:
    <br>- Companies that are already reporting to the SEC (e.g., public companies),
    <br>- Investment companies (e.g., hedge funds, mutual funds),
    <br>- Certain bad actors (individuals or companies with securities law violations).
    <br>- It's important for businesses to assess their eligibility based on the specific rules outlined in the Regulation D exemption.</p>
                             
    <p><u><b>11. Is there a limit to how many rounds of funding I can do under Rule 504?</u></b><br>
    • Answer: There is no explicit limit on the number of rounds a company can conduct under Rule 504, but you are limited to raising $10 million in a 12-month period. If you raise more than that in any rolling 12-month period, you will exceed the cap and may need to consider other methods of fundraising, such as Regulation D Rule 506.</p>
                             
    <p><u><b>12. How does Rule 504 compare to other Regulation D exemptions, like Rule 506(b) or 506(c)?</u></b><br>
    • Answer: The main differences between Rule 504 and other Regulation D exemptions are:
    <br>- Fundraising Limits: Rule 504 allows companies to raise up to $10 million, whereas Rule 506(b) and 506(c) allow for unlimited fundraising but have different investor requirements (506(b) limits to accredited investors, while 506(c) allows general solicitation but limits to accredited investors).
    <br>- Investor Types: Rule 504 allows both accredited and non-accredited investors (with limits on non-accredited investors), whereas 506(b) restricts you to only accredited investors, and 506(c) allows general solicitation but requires verification of accredited investor status.
    <br>- Compliance: Rule 504 typically involves less stringent compliance than Rule 506(c) and may be more suitable for companies seeking a moderate amount of capital from a broad base of investors.
    </p> 
                             
    <p><u><b>13. Can my company raise capital using Rule 504 if we have already raised funds previously?</u></b><br>
    • Answer: Yes, you can still use Rule 504 to raise capital even if you have raised funds in the past, as long as you don’t exceed the $10 million cap in a 12-month period. It’s important to track all prior capital raised under the exemption to ensure you stay within the limits.</p>

    <p><u><b>14. What should a company consider before choosing Rule 504 as its capital-raising method?</u></b><br>
    • Answer: Before using Rule 504, companies should:
    <br>- Assess the amount of capital needed (up to $10 million).
    <br>- Determine if they are prepared for the legal and compliance costs.
    <br>- Evaluate whether they can handle general solicitation and the associated marketing costs.
    <br>- Understand the restrictions on non-accredited investors and how to properly disclose necessary information.
    <br>- Consider the time it will take to prepare the offering and attract investors.</p>                         
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd504_twelve(request):
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
    Capital Type: Rule 504</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    The ideal stage for a company to use Regulation D Rule 504 is typically early-stage, with growth potential, a need for capital for specific projects or expansions, and a target audience of both accredited and non-accredited investors.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    The ideal entity types for a business looking to use Regulation D Rule 504 are primarily LLCs and C Corporations. LLCs are typically the best fit for early-stage companies because of their flexibility, tax advantages, and ease of management. C Corporations are suitable if the company is looking to scale rapidly, attract institutional investors, or potentially go public in the future. While S Corporations and Limited Partnerships can also use Rule 504, they have limitations that make them less optimal in many cases.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    Under Regulation D Rule 504, there are no specific restrictions regarding the amount of pre-existing capital a business has raised before using this rule. A company can use Rule 504 to raise funds even if it has previously raised capital through other means, including venture capital, other private offerings, or previous Regulation D exemptions. 
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    A company can raise capital through Rule 504 regardless of its previous fundraising but it must stay within the $10 million limit across all capital raised in the past 12 months and ensure compliance with other regulatory requirements, such as investor type, state laws, and solicitation rules. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    A company can raise up to $10 million in a 12-month period using Regulation D Rule 504.
    <br>This is the maximum amount allowed under Rule 504 for a single offering, and it applies to both equity and debt securities.</p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Regulation D Rule 504 is most ideal for companies in the seed or early-stage of development that need to raise up to $10 million in capital. These companies typically have a smaller capital requirement, are still refining their business model, and seek funding from a wide range of investors, including both accredited and non-accredited investors. More mature companies or those seeking larger capital infusions typically explore other options like Regulation D Rule 506 for larger rounds.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    There is no limit on the number of tranches a company can have under Regulation D Rule 504 as long as the total amount raised does not exceed $10 million in any 12-month period. You can raise the capital in multiple rounds, but once the $10 million limit is reached, no further capital can be raised.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    When a business raises capital through Regulation D Rule 504, there are no specific restrictions on how the funds must be used, meaning the company has considerable flexibility in allocating the capital raised.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    A business looking to use Regulation D Rule 504 should have a moderate to high level of risk tolerance and be prepared for uncertainty, complex regulatory compliance, and potential challenges in managing investor relationships. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    A company raising capital under Regulation D Rule 504 should have a moderate to high level of capital cost tolerance. While the legal and compliance costs are typically lower than those for a registered offering, the company will still incur substantial costs in areas like legal advice, marketing, administrative support, and investor management.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    The upfront costs for a company raising capital under Regulation D Rule 504 can vary widely depending on factors like the complexity of the offering, the number of states involved, the need for intermediaries, and the company’s specific industry. However, an average estimate for upfront costs typically falls within the range of $25,000 to $75,000 or more. This range includes several key expenses that a business will incur when using Rule 504 to raise capital.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    A company can typically raise capital under Regulation D Rule 504 in 6 to 12 weeks if everything is well-prepared. The process can be quicker (around 6 to 8 weeks) if the offering is straightforward, the legal and compliance aspects are efficiently handled, and the company uses effective solicitation methods.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)