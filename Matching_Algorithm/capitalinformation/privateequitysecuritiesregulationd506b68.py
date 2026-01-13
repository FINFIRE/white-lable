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


def privateequitysecuritiesregulationd506b(request):
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Private Equity Securities</b></u><br>
    Capital Type: Rule 506(b) of Regulation D (Title II of the JOBS Act)</center></p>
    <p><b><u>Introduction</u></b><br>
    According to the SBAO Report, Rule 506(b) remains the overwhelming choice for capital raises
     among small businesses, with a total offering of $2.7 Trillion and a median raise of 
     $1.2 Million. Once again, the aggregate amount raised under Rule 506(b) far outstripped the 
     amount raised via initial public offerings (IPO), which raised only $17 Billion. <a href=" https://www.jdsupra.com/legalnews/rule-506-offerings-continue-to-be-7760214/">Regulation A 
     offerings, often called “mini-IPOs,” raised $1.5 Billion.</a></p>

    <p><b><u>Definition of Capital Type</b></u><br> 
    1) Rule 506(b) of Regulation D is considered a “safe harbor” under Section 4(a)(2). 
    It provides objective standards that a company can rely on to meet the requirements of the 
    Section 4(a)(2) exemption. Companies conducting an offering under Rule 506(b) can raise an 
    unlimited amount of money and can sell securities to an unlimited number of accredited investors. 
    An offering under Rule 506(b), however, is subject to the following requirements:
    <br>•	No general solicitation or advertising to market the securities
    <br>•	Securities may not be sold to more than 35 non-accredited investors (all non-accredited 
    investors, either alone or with a purchaser representative, must meet the legal standard of 
    having sufficient knowledge and experience in financial and business matters to be capable of 
    evaluating the merits and risks of the prospective investment).</p>

    <p>If non-accredited investors are participating in the offering, the company conducting the offering:
    <br>•	Must give any non-accredited investors disclosure documents that generally contain the same type of information as provided in Regulation A offerings (the company is not required to provide specified disclosure documents to accredited investors, but, if it does provide information to accredited investors, it must also make this information available to the non-accredited investors as well)
    <br>•	Must give any non-accredited investors financial statement information specified in Rule 506
    <br>•	Should be available to answer questions from prospective purchasers who are non-accredited investors
    </p>
                             
    <p>Purchasers in a Rule 506(b) offering receive “restricted securities." A company is 
    required to file a notice with the Commission on Form D within 15 days after the first sale of 
    securities in the offering. Although the Securities Act provides a federal preemption from state 
    registration and qualification under Rule 506(b), the states still have authority to require 
    notice filings and collect state fees.</p>
                             
    <p>Rule 506(b) offerings are subject to “bad actor” disqualification provisions. (SEC, 2024)</p>

    <p>2) Section 4(a)(2) of the Securities Act exempts from registration “transactions by an issuer 
    not involving any public offering.” Rule 506(b) is a rule under Regulation D that provides 
    conditions that an issuer may rely on to meet the requirements of the Section 4(a)(2) exemption. 
    One of these conditions is that an issuer must not use general solicitation to market the 
    securities. “General solicitation” includes advertisements published in newspapers and magazines,
    public websites, communications broadcasted over television and radio, and seminars where 
    attendees have been invited by general solicitation or general advertising. In addition, the use
    of an unrestricted, and therefore publicly available, website constitutes general solicitation.
    The solicitation must be an “offer” of securities, but solicitations that condition the market 
    for an offering of securities may be considered offers as well. (Smith, 2021)</p>

    <p>3) Purchasers of securities offered pursuant to Rule 506 receive "restricted" securities, 
    meaning that the securities cannot be sold for at least six months or a year without registering 
    them.</p>   

    <p>Companies that comply with the requirements of Rule 506(b) do not have to register their 
    offering of securities with the SEC, but they must file what is known as a "Form D" electronically 
    with the SEC after they first sell their securities. Form D is a brief notice that includes the 
    names and addresses of the company’s promoters, executive officers and directors, and some details
     about the offering, but contains little other information about the company.  You can access the 
     SEC’s EDGAR database to determine whether the company has filed a Form D.</p>

    <p>Be sure to ask whether your state regulator has received notice of the offering for sale 
    in your state. (Rule 506 of Regulation D, n.d.)</p>



    <p><b><u>References</b></u><br> 
    Rule 506 of Regulation D. (n.d.). Retrieved from Investor: 
    <br><a href="https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-506-regulation-d">https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-506-regulation-d</a><></p>

    <p>SEC. (2024, November 14). Private Placements - Rule 506(b). Retrieved from SEC:<br>
    <a href="https://www.sec.gov/resources-small-businesses/exempt-offerings/private-placements-rule-506b">https://www.sec.gov/resources-small-businesses/exempt-offerings/private-placements-rule-506b</a></p>

    <p>Smith, T. D. (2021). Business Capital 101. In T. D. Smith, Business Capital 101 (p. 25). 
    San Francisco: Imaginary Press.</p>

    <p><b><u>Legal Qualification Requirements</u></b> 
    <br>•	The business must be a domestic entity (e.g., corporation, LLC, or partnership) 
    <br>•	Securities may not be sold to more than 35 non-accredited investors
    <br>•	The company cannot engage in general solicitation (advertising or public promotions). Securities must be offered privately, and there must be a pre-existing relationship with investors or proper vetting of potential investors.
    <br>•	The securities must be private, meaning they cannot be listed on public exchanges or registered with the SEC. 
    <br>•	While Rule 506(b) provides a federal exemption, the company must still comply with state securities regulations (Blue Sky Laws) This often involves notice filings and paying applicable state fees.
    <br>•	Filing Form D: This form provides basic information about the issuer and the offering.
    <br>•	Non-accredited investors can be involved, but their number must not exceed 35. These investors must also have the knowledge to evaluate the investment.
    <br>•	No “Bad Actor” Disqualifications. The company and its key people (e.g., executives, directors) cannot have a history of criminal violations or SEC sanctions.
    <br>•	The business must have a lawful management structure and must be an actively operating company. It should not be a "shell" company created solely for raising capital.
    <br>•	The issuer must provide sufficient disclosures to potential investors about the risks of the investment. While not required, a Private Placement Memorandum (PPM) is recommended to ensure transparency.
    </p>
                             
    <p><b><u>Supporting Document List</u></b> 
    <br>•	Private Placement Memorandum (PPM): A detailed document outlining the offering, including the company's business, financials, risk factors, and the use of funds. While not legally required, it is highly recommended for full investor disclosure.
    <br>•	Subscription Agreement: A binding agreement where investors commit to purchasing securities, including details on the amount, price, and the investor’s accredited status.
    <br>•	Accredited Investor Verification: Documentation to confirm that investors meet the SEC's definition of accredited investors. This may include financial statements, tax returns, or third-party confirmation.
    <br>•	Form D (Notice of Exemption): A filing with the SEC within 15 days of the first securities sale, notifying the SEC that the offering is exempt under Regulation D. This includes basic company details and the amount of capital raised.
    <br>•	Financial Statements: Companies must provide investors with financial documents like balance sheets and income statements. Audited statements may be required if the offering exceeds $5 million.
    <br>•	Investor Questionnaire: A form completed by investors to assess their accredited status and suitability for the investment, asking about income, net worth, and investment experience.
    <br>•	Operating Agreement / Articles of Incorporation / Corporate Bylaws: Governing documents of the company (LLC operating agreement or corporate bylaws) that outline the company’s structure, management, and investor rights.
    <br>•	State Filings (Blue Sky Filings): Additional filings required by state regulators to comply with state securities laws. This includes submitting notices and paying filing fees for each state where securities are sold.
    <br>•	Capitalization Table (Cap Table): A detailed list showing the company’s securities and ownership distribution, including shares, options, and other securities, both before and after the offering.
    <br>•	Subscription Documents and Instructions: Detailed instructions for investors on how to complete and submit their subscription agreements and other related documents.
    <br>•	Marketing Materials (if applicable): While general solicitation is prohibited, materials shared with prospective investors must align with the offering documents, avoiding misleading statements.  
    </p>   
        """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506bfaq(request):
    introduction = mark_safe("""
    <p><center>Capital Market: Private Equity Securities<br>
    Capital Type: Rule 506(b) of regulation D (Title II of the JOBS Act)</center></p>                        
    <p><center><u><b>Frequently Asked Question for Regulation D 506(b)</u></b></center></p>
    <p><u><b>1. What is Rule 506(b) of Regulation D, and how does it differ from other capital-raising options?</u></b><br>
    • Answer: Rule 506(b) is part of Regulation D, a SEC exemption that allows companies to raise capital without having to
     register securities with the SEC. Unlike public offerings, Rule 506(b) allows an unlimited 
     amount of capital to be raised from accredited investors (and up to 35 non-accredited investors, 
     with certain requirements). It differs from other options like Rule 506(c), which allows for 
     general solicitation, but only permits sales to accredited investors.</p>
                             
    <p><u><b>2. Why should I choose Rule 506(b) over other options like Regulation A or Rule 506(c)?</u></b><br>
    • Answer:  Rule 506(b) offers the flexibility of raising an unlimited amount of capital, and it does not require 
    general solicitation, which might be a good option for companies with established relationships or
     networks of accredited investors. It’s a good choice if you want to avoid the complexity and 
     additional costs of Regulation A offerings or the public nature of Rule 506(c), which requires 
     advertising to only accredited investors.</p>
                             
    <p><u><b>3.Who can invest in my offering under Rule 506(b)?</u></b><br>
    • Answer: You can sell securities to an unlimited number of accredited investors and up to 35 
    non-accredited investors, but the latter must meet specific sophistication requirements. 
    Non-accredited investors must have enough financial knowledge or experience to evaluate the 
    investment risks and make informed decisions.</p>
                             
    <p><u><b>4. What is the definition of an accredited investor under Rule 506(b)?</u></b><br>
    • Answer: An accredited investor is typically:<br>
    -An individual with an annual income of $200,000 ($300,000 for married couples) for the last two 
    years, with the expectation of the same income in the current year.<br>
    -An individual with a net worth exceeding $1 million, excluding their primary residence.<br>
    -Certain entities like banks, insurance companies, and large investment funds are also considered accredited.</p>
                             
    <p><u><b>5. Can I solicit investors publicly under Rule 506(b)?</u></b><br>
    • Answer: No. Rule 506(b) prohibits general solicitation or advertising to the public. 
    You must have a pre-existing relationship with investors or ensure they are otherwise carefully 
    vetted. This contrasts with Rule 506(c), which allows general solicitation but restricts sales to 
    accredited investors only.</p>
                             
    <p><u><b>6. What are the filing requirements for Rule 506(b)?</u></b><br>
    • Answer: You must file Form D with the SEC within 15 days after the first sale of securities. 
    This form provides basic details about the offering and the company. Additionally, you may need 
    to file notices with state regulators (Blue Sky filings) to comply with state securities laws, 
    though Rule 506(b) offers a federal exemption from state registration.</p>
                             
    <p><u><b>7. Can I raise an unlimited amount of capital under Rule 506(b)?</u></b><br>
    • Answer: Yes, Rule 506(b) allows you to raise unlimited capital from accredited investors,
     which makes it an attractive option for large fundraising rounds.</p>
                             
    <p><u><b>8. What are the investor accreditation verification requirements under Rule 506(b)?</u></b><br>
    • Answer: You must verify that your investors are accredited, typically through:
    <br>-Reviewing financial documents such as tax returns or bank statements.
    <br>-Using third-party verification services (e.g., a broker-dealer or investment advisor).
    <br>-Investors may also complete an accredited investor questionnaire.
    <br>-The level of verification needed depends on the nature of the offering and the investors.</p>
                             
    <p><u><b>9.Are there any risks or disadvantages to using Rule 506(b)?</u></b><br>
    • Answer: The main limitation of Rule 506(b) is the no general solicitation restriction, which 
    may make it harder to reach a large pool of potential investors compared to options like Rule 
    506(c) or Regulation A. Additionally, managing investor relationships and ensuring compliance 
    with accreditation requirements can be more complex for companies unfamiliar with the process.</p>
                             
    <p><u><b>10. Do I need a Private Placement Memorandum (PPM) when using Rule 506(b)?</u></b><br>
    • Answer:No, a PPM is not legally required under Rule 506(b). However, it is highly recommended because 
    it ensures full disclosure to investors about the risks, business model, and terms of the offering.
     A well-prepared PPM can help reduce the risk of legal disputes or claims of misinformation.</p>
                             
    <p><u><b>11. Can I include non-accredited investors in my offering?</u></b><br>
    • Answer: Yes, you can include up to 35 non-accredited investors, but they must be sophisticated.
     This means they must have sufficient financial knowledge to assess the risks involved in the 
     investment. You need to carefully vet these investors and ensure they meet the SEC's 
     sophistication standards.</p>
                             
    <p><u><b>12. What are the key legal requirements and restrictions for using Rule 506(b)?</u></b><br>
    • Answer: The company must not have been involved in bad actor disqualifications (e.g., criminal violations or SEC sanctions).
    The company must ensure proper disclosures to investors.
    It must comply with state securities laws (Blue Sky laws).
    The business must be an actively operating entity and not a shell company.</p>
                             
    <p><u><b>13. How does Rule 506(b) impact my business's ability to raise capital internationally?</u></b><br>
    • Answer: Rule 506(b) is a U.S.-based exemption, meaning it applies to U.S.-based companies 
    raising capital from U.S. investors. If you plan to raise capital from international investors, 
    you will need to ensure that the offering complies with the laws and regulations of the 
    respective foreign jurisdictions.</p>
                             
    <p><u><b>14. How long does it take to complete a Rule 506(b) offering?</u></b><br>
    • Answer:  The timeline can vary depending on the size and complexity of the offering,
     but generally, a Rule 506(b) offering can take anywhere from a few weeks to a few months. 
     This depends on how quickly you can secure investor commitments, prepare the necessary 
     documentation (PPM, Form D, etc.), and meet all regulatory requirements.</p> 
                             
    <p><u><b>15. What are the costs associated with using Rule 506(b)?</u></b><br>
    • Answer: The costs include:
    <br>-Legal fees for preparing the offering documents, such as a PPM, subscription agreements, and ensuring compliance with securities laws.
    <br>-Filing fees for submitting Form D and any state securities filings.
    <br>-Potential third-party verification fees for accrediting investors.
    <br>-Miscellaneous administrative costs related to managing investor relations and documentation.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def privateequitysecuritiesregulationd506btwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Private Equity Rule 506(b) of Regulation D (Title II of the JOBS Act)</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    While {n} is in the {stage} stage, utilizing Private Equity Rule 506(b) of Regulation D 
    (Title II of the JOBS Act) offers several strategic advantages. Rule 506(b) is ideal for companies 
    in the {stage} stage looking to scale operations, engage a network of accredited investors, and 
    raise funds more efficiently while maintaining compliance with SEC regulations. Rule 506(b) 
    enables you to target high-net-worth individuals and institutional investors, offering greater 
    flexibility in structuring your offering.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Utilizing Private Equity Rule 506(b) of Regulation D (Title II of the JOBS Act) for a {entity} provides flexibility in terms of funding structure and investor outreach, with fewer 
    regulatory burdens compared to traditional methods like venture capital or an IPO. It also enables 
    you to engage a targeted investor pool, which is ideal for scaling the business quickly and 
    efficiently.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    {n} has already raised {preraise} in pre-capital so raising capital utilizing Private Equity Rule 
    506(b) of Regulation D (Title II of the JOBS Act) offers flexibility in structuring the offering 
    and the ability to target accredited and non-accredited investors.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    {n} has already raised {preraise} through a {premarket} so utilizing Private Equity Rule 506(b) 
    of Regulation D (Title II of the JOBS Act) offers faster access to significant capital compared 
    to traditional fundraising routes, enabling Dining Empire to effectively engage with a targeted 
    group of investors while scaling its operations.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Private Equity Rule 506(b) of Regulation D (Title II of the JOBS Act) allows businesses to raise 
    an unlimited amount of capital from accredited investors over a 12-month period, providing significant 
    flexibility for your goal of raising {raisegoal}.
    </p>
    
    <p><b><u>6 - Capital Round Assessment</b></u><br>
    While {n} is engaged in the {rounds} of capital raising, Private Equity Rule 
    506(b) of Regulation D (Title II of the JOBS Act) allows you to raise funds from accredited 
    investors and non-accredited investors, offering access to a large investor base. The capital 
    raised can be used for scaling operations, marketing, and growing human capital, making Rule 
    506(b) a strong option for early-stage businesses looking to raise substantial capital and 
    accelerate growth.</p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Since you're planning to raise capital in {tranch} tranches within a 12-month period, Private Equity 
    Rule 506(b) of Regulation D (Title II of the JOBS Act) offers the flexibility to structure your 
    offering in multiple stages, allowing you to align the fundraising process with your specific 
    business needs and funding objectives.</p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Private Equity Rule 506(b) of Regulation D (Title II of the JOBS Act) offers significant flexibility
    in how funds raised can be used, with no specific restrictions on their allocation. This makes it 
    an ideal solution for addressing the diverse financial needs of your business. While you will 
    need to clearly specify these intended uses in the offering documents to ensure compliance and 
    transparency with investors, Rule 506(b) allows you to raise capital for purposes such as:<b>note(should be used from this list: {useoffund})</b>
    <br>1.	Startup – Working Capital
    <br>2.	Growth Scalability
    <br>3.	Marketing & Sales
    <br>4.	Cash Flow Capital
    <br>5.	Human Capital
    <br>6.	Other</p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Private Equity Rule 506(b) of Regulation D (Title II of the JOBS Act) allows you to present an 
    investment opportunity to a targeted group of investors who are typically seeking higher returns 
    and are interested in high-growth, early-stage companies. This aligns well with {n} 
    growth objectives. Under Rule 506(b), you have the flexibility to offer various types of 
    securities depending on what best fits your business model and investor preferences. Since your 
    company has already raised capital through {premarket}, you can continue with this structure or choose 
    to offer equity in exchange for the capital raised. 
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The principle’s willingness to accept {enterprisecost} costs enables the company to manage the
    expenses associated with a public offering under Private Equity Rule 506(c) of Regulation D
    (Title II of the JOBS Act), while leveraging the funds to drive strategic growth, broaden the
    investor base, and position the company for long-term success. This approach provides the
    flexibility to engage with investors who are typically seeking higher returns.</p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>With a {upfrontcost} budget, Rule 506(b) of Regulation D may be a challenging option unless you are able to leverage existing networks of investors and manage legal and verification costs efficiently. For smaller budgets, Regulation CF or other private placements might be more feasible options to raise capital while keeping expenses manageable.
    Low-end estimate: $10,000 - $15,000 (with minimal legal and marketing involvement)
    High-end estimate: $30,000 - $50,000 or more (with a full-scale offering, legal representation, and non-accredited investor disclosures)</p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <b>NOTE NEED A DYNAMIC RESPONSE!!!</b>The capital-raising process under Rule 506(b) of Regulation D can typically take 3 to 6 months 
    depending on how efficiently you manage the offering. It could take as little as {upfronttime} if 
    you already have a solid investor network and streamlined processes in place, but be prepared for 
    a longer timeline if you're starting from scratch or targeting a larger pool of investors.</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'name':name,
        'introduction':introduction,
    }
    return render(request,'detail.html',context)