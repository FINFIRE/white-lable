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


def royaltyfinancing(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Definition of Capital Market: Royalty Financing</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Royalty financing is ideal for companies generating consistent revenue and seeking non-dilutive capital in amounts typically ranging from $100,000 to $20 million, depending on the investor and company revenue. It is designed so that the issuer may receive upfront capital in exchange for a fixed percentage of future gross revenue until a pre-agreed return cap is met. {n} fits that definition. Royalty financing has been a viable tool for growth-stage companies for over a decade. For example, Clearco, a leading royalty and revenue-based financing firm, surpassed $3 billion in capital deployed to e-commerce and SaaS companies using this model in 2023. In that same year, platforms like Pipe and Braavo collectively advanced hundreds of millions in royalty-based capital to recurring-revenue businesses. On average, most royalty financing agreements target a 1.5x to 3x repayment cap and offer founders a flexible, non-dilutive alternative to traditional equity or debt. However, one of the primary risks for companies is the impact on cash flow, as a portion of revenue is continuously diverted to repay the investor, which can strain finances during slower sales periods.
    </p>
                                 
    <p><b><u>Definition of Capital Type</u></b><br>
    <br>1. Royalty financing, also known as revenue-based financing, is a form of alternative funding where a company receives upfront capital in exchange for a percentage of its future gross revenues. Unlike traditional equity financing, it does not require giving up ownership or shares, and unlike traditional loans, it doesn’t involve fixed monthly payments or interest rates. Instead, repayments are tied directly to the company’s revenue, making it a flexible option—especially for businesses with predictable income streams like SaaS, e-commerce, or subscription-based models. The agreement continues until a predetermined repayment cap (often 1.5x to 3x the original investment) is reached. (Hayes, 2022)
<br>
    <br>2. Royalty financing, also known as revenue-based financing, comes in several forms depending on the structure of repayment and the source of funds. Traditional royalty financing involves a company receiving capital in exchange for agreeing to pay a fixed percentage of future revenues until a set return multiple (often 1.5x–3x the original investment) is reached. Synthetic royalty financing, more common in biotech or energy sectors, involves projected future revenue streams based on patents or licenses being used as collateral. Milestone-based royalty deals tie repayments to performance triggers such as product launches or revenue targets. Royalty buyouts occur when investors provide a lump sum upfront in exchange for acquiring the rights to an existing revenue-generating asset, like music catalogs or IP licenses. Each type offers different risk-return dynamics and is best suited to different business models and maturity levels. (Trattner, T., Murr, R. A., Gibson Dunn, Jin Hee Kim, & Jeff Krause, 2025)
<br>
    <br>3. Royalty financing has evolved over decades, with its origins tracing back to the early 20th century, primarily in the oil and gas industry. Initially, this form of financing was used by natural resource companies to raise capital without giving up equity. Over time, royalty financing expanded to other industries, particularly in the entertainment, pharmaceuticals, and technology sectors. The model gained significant traction in the 1980s and 1990s as a means for companies, especially in the life sciences, to raise funds without diluting ownership or taking on traditional debt. In the 2000s, as intellectual property rights became more valuable, royalty financing began to be seen as an innovative way for companies to monetize future revenue streams, such as patents, trademarks, and other intangible assets. Today, royalty financing is used across various sectors and has grown into a sophisticated and widely accepted alternative to traditional forms of capital raising. It provides companies with non-dilutive capital, allowing them to retain control while still securing the funds needed for growth or development. (Royalty financing: an appealing alternative to traditional life sciences financing, 2024)
<br>
    <br>4. Royalty financing offers a flexible, non-dilutive way for companies to raise capital, but it comes with certain risks. One significant risk is the repayment structure—companies are required to pay a percentage of future revenues, which can become burdensome during periods of lower-than-expected sales. This can limit cash flow and impact operations, especially for companies in volatile industries. Additionally, the cost of capital in royalty financing can be higher than traditional loans, as investors typically demand a higher return due to the risks they are taking on. There is also the risk of overpaying if the business performs better than expected, as royalties are tied to future earnings. Finally, the need to comply with detailed terms and agreements can be complex and restrictive, potentially affecting future flexibility in managing business operations and making strategic decisions. (Faster Capital, n.d.)
<br>
    <br>5. To raise money via royalty financing, a company needs to demonstrate stable, predictable revenue streams, usually from intellectual property (IP), products, or services with long-term market viability. It should have a proven track record of generating significant revenue, often from established products or a strong brand reputation. Investors will look for detailed financial records, including past sales data, future revenue projections, and a clear understanding of how royalties will be structured. Additionally, a company must be prepared to negotiate favorable terms that protect its future revenue while meeting investor expectations. The company should also have a solid business plan, legal agreements related to IP or products, and a clear exit strategy for repaying investors, whether through a set period or a percentage of revenue. (Faster Capital, n.d.)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Hayes, A. (2022, December 22). Revenue-Based financing: Definition, how it works, and example. Investopedia. <a href="https://www.investopedia.com/terms/r/revenuebased-financing.asp">https://www.investopedia.com/terms/r/revenuebased-financing.asp</a>
<br>
    <br>Trattner, T., Murr, R. A., Gibson Dunn, Jin Hee Kim, & Jeff Krause. (2025). Royalty Finance: Structures and Trends. <a href="https://www.law.berkeley.edu/wp-content/uploads/2025/04/Royalty-Financings-Overview_-April-2025v2_108990820_2.pdf">https://www.law.berkeley.edu/wp-content/uploads/2025/04/Royalty-Financings-Overview_-April-2025v2_108990820_2.pdf</a>
<br>
    <br>Royalty financing: an appealing alternative to traditional life sciences financing. (2024, May 8). Debevoise. <a href="https://www.debevoise.com/insights/publications/2019/11/royalty-financing-an-appealing-alternative-to?">https://www.debevoise.com/insights/publications/2019/11/royalty-financing-an-appealing-alternative-to?</a>
<br>
    <br>The risks associated with Royalty financing - FasterCapital. (n.d.). FasterCapital. <a href="https://fastercapital.com/content/The-risks-associated-with-Royalty-financing.html">https://fastercapital.com/content/The-risks-associated-with-Royalty-financing.html</a>
<br>
    <br>Royalty financing: How to get funding and pay back based on your revenue - FasterCapital. (n.d.). FasterCapital. <a href="https://fastercapital.com/content/Royalty-financing--How-to-get-funding-and-pay-back-based-on-your-revenue.html?">https://fastercapital.com/content/Royalty-financing--How-to-get-funding-and-pay-back-based-on-your-revenue.html?</a>    
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
     <br>• Business Entity: Must be a legally registered company (e.g., LLC, corporation).
     <br>• Revenue-Generating Assets: Must own valuable IP or assets that generate revenue for royalty payments.
     <br>• Securities Compliance: Comply with securities laws if offering securities alongside royalty agreements.
     <br>• Financial Records: Maintain accurate financial records (e.g., income statements, projections).
     <br>• Due Diligence: Be ready for investor due diligence, providing legal, financial, and operational documents.
     <br>• Tax Compliance: Ensure the company is in good standing with tax authorities.
     <br>• Contractual Authority: Have the legal authority to enter into royalty agreements.
     <br>• No Major Legal Issues: Avoid ongoing litigation that could affect the company’s obligations.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Entity: Must be a legally registered company (e.g., LLC, corporation).
    <br>• Revenue-Generating Assets: Must own valuable IP or assets that generate revenue for royalty payments.
    <br>• Securities Compliance: Comply with securities laws if offering securities alongside royalty agreements.
    <br>• Financial Records: Maintain accurate financial records (e.g., income statements, projections).
    <br>• Due Diligence: Be ready for investor due diligence, providing legal, financial, and operational documents.
    <br>• Tax Compliance: Ensure the company is in good standing with tax authorities.
    <br>• Contractual Authority: Have the legal authority to enter into royalty agreements.
    <br>• No Major Legal Issues: Avoid ongoing litigation that could affect the company’s obligations.
    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def royaltyfinancingfaq(request):
    introduction = mark_safe("""            
    <p><b><u>FAQs</u></b></p>
                             
    <p><b><u>1. What is royalty financing?</u></b><br>
    • Answer: Royalty financing is a method where a company receives capital in exchange for a percentage of future revenue or sales from a specific asset, typically intellectual property or a product.
    </p>
                             
    <p><b><u>2. How does royalty financing work?</u></b><br>
    • Answer: The company raises money by offering a portion of its future revenue from a particular product or asset (like patents, trademarks, or music) in exchange for upfront capital.
    </p>
                             
    <p><b><u>3. Who benefits from royalty financing?</u></b><br>
    • Answer: Companies looking for non-dilutive funding to finance growth or development, particularly in industries with strong intellectual property or predictable revenue streams.
    </p>
                             
    <p><b><u>4. What are the advantages of royalty financing?</u></b><br>
    • Answer: Royalty financing allows companies to raise capital without giving up equity or taking on debt. It is flexible and linked to future performance, which means repayments are tied to revenue generation.
    </p>
                             
    <p><b><u>5. What are the disadvantages of royalty financing?</u></b><br>
    • Answer: The main drawback is the cost of capital, as investors typically demand a higher return for taking on the risk. It can also be a less favorable option if the company’s revenue projections do not meet expectations.
    </p>
                             
    <p><b><u>6. What types of companies use royalty financing?</u></b><br>
    • Answer: Companies in industries with strong intellectual property assets such as technology, entertainment, pharmaceuticals, and energy often use royalty financing to fund development or expansion.
    </p>
                             
    <p><b><u>7. How are royalties calculated?</u></b><br>
    • Answer: Royalties are typically calculated as a fixed percentage of revenue generated from the asset or product that the investor is funding.
    </p>
                             
    <p><b><u>8. Is royalty financing a long-term or short-term funding option?</u></b><br>
    • Answer: It is usually considered a short to medium-term financing option, with the length of the agreement depending on the time it takes for the company to generate sufficient revenue to repay the investor.
    </p>
                             
    <p><b><u>9. Can royalty financing affect the company’s control?</u></b><br>
    • Answer: Since royalty financing does not involve equity, the company maintains full control. However, it may give investors a say in certain operational aspects related to the product or asset generating royalties.</p>
                             
    <p><b><u>10. What industries are best suited for royalty financing?</u></b><br>
    • Answer: Industries with high-value intellectual property, recurring revenue models, or predictable cash flows, such as technology, pharmaceuticals, entertainment, and energy, are typically best suited for royalty financing.
    </p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def royaltyfinancingtwelve(request):
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
    premarketStr = ''

    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'this model remains financially inefficient as more upfront cost might be required for royalty financing deal.',
        'Minimum $500 - Maximum $999' :  'this model remains financially inefficient as more upfront cost might be required for royalty financing deal.',
        'Minimum $1000 - Maximum $2499' :  'this model remains financially inefficient as more upfront cost might be required for royalty financing deal.',
        'Minimum $2500 - Maximum $4999' :  'this model remains financially efficient however more upfront cost might be required for royalty financing deal.',
        'Minimum $5000 - Maximum $9999' :  'this model remains financially efficient and founder friendly.',
        'Minimum $10000 - Maximum $24999' : 'this model remains financially efficient and founder friendly.',
        'Minimum $25000 - Maximum $49999' : 'this model remains financially efficient and founder friendly.',
        'More than $50000+' : 'this model remains financially efficient and founder friendly.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'required time is not a direct match to with this capital market option',
        '1 Week to 2 Week' : 'required time is not a direct match to with this capital market option',
        '2 Weeks to 4 Weeks' : 'required time matches with this option',
        '1 Month to 2 Months' : 'required time matches with this option',
        '2 Months to 3 Months' : 'required time matches with this option',
        '3 Months to 6 Months' : 'required time matches with this option',
        '6 Months to 12 Months' : 'required time matches with this option',
        'More than 1 year' : 'required time matches with this option',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Royalty Financing</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    {n} is currently in a {stage} stage. This stage is ideal for royalty financing, which allows the company to access capital without equity dilution or fixed debt service. Revenue-based repayments provide flexibility during scaling and align investor returns with business performance.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    As a U.S.-based for-profit entity structured as an {entity}, {n} qualifies for royalty financing. Most revenue-based investors prioritize business model sustainability and clean financials over legal form. Maintaining up-to-date corporate records and GAAP-compliant financials will streamline the diligence process.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} already secured in pre-capital, {n} demonstrates early validation and operational maturity. Royalty investor's view this as a de-risking factor, as it suggests disciplined capital management and an existing foundation of market traction. This can support more favorable repayment terms and investor confidence.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    To date, {n}’s funding has come through {premarketstr}. Royalty financing now offers a non-dilutive option to build on that capital stack, especially well-suited for expanding operations, scaling sales, or increasing inventory—all while preserving founder equity.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    {n} plans to raise a total of {raisegoal}. A portion of this capital—up to $5M depending on revenues—can be structured via royalty financing. This approach supports a balanced capital stack that reduces dilution and maintains operational control. Investors will expect detailed revenue projections to inform repayment scenarios.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Royalty financing is not structured as a conventional capital round (e.g., Seed, Series A) but rather as alternative growth capital. It can complement equity rounds or act as a standalone raise. For XYZ Company, this model is ideal for funding working capital and customer acquisition without triggering valuation negotiations or giving up governance rights.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Royalty financing is often disbursed as a lump sum, though in some cases, drawdowns may be tied to revenue thresholds or key milestones. {n} can work with investors to align disbursement schedules with specific cash flow needs or project phases, such as seasonal inventory ramps or new market entries.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Royalty capital is most effectively deployed into revenue-generating initiatives. {n} plans to apply the funds toward:
    <br>- Sales and marketing expansion
    <br>- Customer acquisition
    <br>- Inventory and supply chain management
    <br>- Product development
    <br>- Operational scaling
    <br>A clear use-of-funds strategy tied to revenue acceleration will strengthen the investment case.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Royalty financing offers reduced risk compared to traditional debt—repayments are tied to actual revenue and pause or scale during revenue dips. However, {n} must show strong gross margins, revenue consistency, and sufficient free cash flow. Investors will also look for safeguards such as minimum revenue thresholds and repayment caps (typically 1.3x–2x of the investment).
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The effective cost of capital is defined by the repayment multiple, typically between 1.3x and 2.0x of the principal. While this may be higher than traditional debt in nominal terms, it offers flexibility and no dilution. For {n}, royalty financing presents predictable cost structure tied directly to performance, with no impact on ownership or control.
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    Royalty financing typically involves low upfront costs. Legal, due diligence, and advisory fees typically range from $2,500 to $10,000, depending on deal complexity. There are no guarantee or underwriting fees. If {n} has a {upfrontcost} allocated for closing costs, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    <br>Royalty financing can often close within 2–8 weeks. Timeline depends on due diligence readiness, investor bandwidth, and documentation. {n}'s {timeanalysis} and can accelerate the process by preparing:
    <br>- Audited or reviewed financials
    <br>- Revenue forecasts
    <br>- Use-of-funds breakdown
    <br>- Customer and retention metrics
    <br>Engaging experienced legal counsel and working with specialized royalty finance providers can further compress the timeline.
    </p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,premarketstr=premarketStr,costanalysis=costanalysis,timeanalysis=timeanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)