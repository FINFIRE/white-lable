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


def venturecapital(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><b><u>Capital Market: Venture Capital</b></u><br></p>
    
    <p><b><u>Introduction</u></b><br>
    Venture capital is ideal for high-growth startups looking to raise equity capital in amounts typically ranging from $1 million to over $100 million, depending on the company’s stage and market potential. It is designed for companies with scalable business models, often in technology, healthcare, and emerging sectors, where institutional investors such as VC firms can provide capital in exchange for ownership equity. {n} fits that definition. Venture capital has been a core engine for innovation and startup growth in the U.S. for decades. For example, in 2023, U.S. venture capital firms invested approximately $170.6 billion across more than 15,000 deals, despite a slowdown from peak pandemic levels. In Q2 2023 alone, $39.8 billion was deployed across 3,011 deals, reflecting renewed investor confidence. The median pre-money valuation for early-stage VC deals in 2023 was $35 million, while late-stage valuations hovered around $90 million.  There are three types of Venture Capital that we can match you with: 1) Venture Capital - Equity Sale, 2) Venture Capital - Long Term Debt and 3) Venture Capital - Mezanine Financing. We will select the most appropriate type of Venture Capital as per your business need.
    </p>
                                 
    <p><b><u>Definition of Capital Market</u></b><br>
    <br>1. Venture capital (VC) is a form of equity financing provided by institutional investors to early-stage, high-potential startups and growth-stage companies in exchange for ownership stakes. It is best suited for businesses with scalable models, innovative products or services, and a strong potential for rapid growth in large markets. Unlike debt financing, VC funding does not require repayment, but it does involve giving up equity and often some level of control, as investors typically seek a say in strategic decisions. Companies pursuing venture capital should be prepared to demonstrate traction, a compelling market opportunity, a capable team, and a clear path to significant return on investment. Venture capital is often used to fund product development, market expansion, hiring, and other key growth initiatives. (Hayes, 2024)
<br>
    <br>2. Venture capital (VC) comes in several forms, each aligned with a company’s stage of growth and risk profile. Seed capital is the earliest type, used to fund initial business development, product research, or proof-of-concept work—typically raised from angel investors or seed-stage VC firms. Startup capital supports companies that have a product or service developed and need funds for early marketing, hiring, or product refinement. Early-stage capital, often classified as Series A or B rounds, helps companies scale operations, expand teams, or accelerate customer acquisition. Expansion capital (or growth-stage VC), which includes Series C and beyond, is aimed at more mature startups that are generating revenue and seeking larger investments to grow rapidly, enter new markets, or prepare for acquisition or IPO. Late-stage VC is geared toward companies close to profitability or exit, often used to strengthen the balance sheet before a public offering. In addition, mezzanine financing and bridge financing are sometimes offered by VCs to help firms transition to IPO or acquisition. Each type serves a specific purpose depending on the company’s development stage and strategic goals. (Types of venture capital funds, 2023)
<br>
    <br>3. Venture capital has its roots in the post–World War II era, when the U.S. government and private investors began seeking ways to fund innovative companies outside of traditional bank financing. The first formal venture capital firm, American Research and Development Corporation (ARDC) was founded in 1946 by Georges Doriot, a Harvard Business School professor. ARDC famously helped fund Digital Equipment Corporation (DEC), generating one of the earliest success stories in VC history. The industry grew slowly until the 1980s, when a surge in tech startups and favorable capital gains tax reforms sparked major expansion. Silicon Valley emerged as the epicenter of venture capital activity, with firms like Kleiner Perkins and Sequoia Capital backing the earliest generations of tech giants. By the 2000s, venture capital had become a global industry, fueling the rise of major companies like Google, Facebook, and Uber, and expanding beyond technology into biotech, fintech, and other sectors. Today, VC continues to evolve, with newer models like micro-VCs, corporate venture arms, and impact investing reshaping the landscape. (The founder of Modern Venture Capital. 2014)
<br>
    <br>4. Raising capital through venture capital can provide rapid growth opportunities, but it also comes with significant risks. One of the primary risks is loss of control—venture capitalists typically require equity ownership and often demand board seats, giving them influence over strategic decisions. This can lead to conflicts in vision, especially if the investors prioritize rapid scaling or exit strategies like IPOs or acquisitions that may not align with the founders’ long-term goals. Additionally, the pressure for high returns can create unrealistic growth expectations, leading startups to scale prematurely or shift focus. If the company underperforms, it risks future fundraising challenges or down rounds, which can dilute founders further and harm company morale. Lastly, rejection rates are high, and the fundraising process itself can be time-consuming, pulling attention away from core operations. (Faster Capital, n.d.)
<br>
    <br>5. To raise money via venture capital (VC), a company typically needs to meet several key requirements. The business should have a scalable model with strong growth potential, particularly in industries like technology, biotech, or fintech. A competent and experienced management team is crucial, as investors often prioritize the leadership behind the company. The company should target a large, growing addressable market, demonstrating that it can support substantial revenue. It should also have a validated product or minimum viable product (MVP), with some traction in the market such as revenue, users, or partnerships. A clear exit strategy, such as an IPO or acquisition, is essential for investors seeking returns. Legally, the company should be structured as a C-corporation, preferably registered in Delaware due to its favorable corporate laws. Additionally, the company must maintain a clean cap table with minimal complications and fair equity splits. Having a unique value proposition or competitive moat, such as intellectual property or technology, is important to stand out in the market. Financial projections for the next 3–5 years and a compelling pitch deck are also necessary to attract VC interest and pass through the rigorous due diligence process. (Lavinsky, 2024)
    </p>
                             
    <p><b><u>References</u></b><br>
    <br>Hayes, A. (2024, October 18). What is venture capital? Definition, pros, cons, and how it works. Investopedia. <a href="https://www.investopedia.com/terms/v/venturecapital.asp?">https://www.investopedia.com/terms/v/venturecapital.asp?</a>
<br>
    <br>Types of venture capital funds: understanding VC stages, financing methods, risks, and more. (2023, November 20). Visible.vc. <a href="https://visible.vc/blog/types-of-venture-capital-funds/">https://visible.vc/blog/types-of-venture-capital-funds/</a>
<br>
    <br>The founder of Modern Venture Capital. (2014, December 23). Harvard Business School. <a href="https://www.library.hbs.edu/working-knowledge/the-founder-of-modern-venture-capital">https://www.library.hbs.edu/working-knowledge/the-founder-of-modern-venture-capital</a>
<br>
    <br>Risks of taking venture capital - FasterCapital. (n.d.). FasterCapital. <a href="https://fastercapital.com/content/Risks-of-taking-venture-capital.html">https://fastercapital.com/content/Risks-of-taking-venture-capital.html</a>
<br>
    <br>Lavinsky, D. (2024, October 29). Venture Capital requirements. Growthink. <a href="https://www.growthink.com/businessplan/help-center/venture-capital-financing-it-within-your-reach?">https://www.growthink.com/businessplan/help-center/venture-capital-financing-it-within-your-reach?</a>
    </p>
                             
    <p><b><u>Qualification Requirements</u></b>
    <br>• Legal Entity: Typically, a C-corporation, often incorporated in Delaware for favorable laws.
    <br>• Clean Cap Table: A well-organized ownership structure.
    <br>• Intellectual Property: Protection of key assets like patents or trademarks.
    <br>• Securities Compliance: Adherence to SEC regulations for stock issuance.
    <br>• Investor Agreements: Clear shareholder agreements outlining rights and obligations.
    <br>• Board of Directors: A structured board, often with VC representation, to guide company decisions.
    </p>
    
                             
    <p><b><u>Supporting Document List</u></b>
    <br>• Business Plan: A detailed document outlining the company’s vision, goals, target market, and financial projections.
    <br>• Pitch Deck: A visual presentation summarizing the company’s business model, market opportunity, financials, and team.
    <br>• Financial Statements: Balance sheet, income statement, and cash flow projections to demonstrate financial health.
    <br>• Cap Table: A detailed capitalization table showing the ownership structure and equity distribution.
    <br>• Legal Documents: Incorporation papers, operating agreements, and any agreements with prior investors.
    <br>• Intellectual Property Documentation: Proof of ownership or patents, trademarks, or copyrights.
    <br>• Market Research: Data supporting the demand and growth potential for the company’s product or service.
    <br>• Team Resumes: Background information on key team members, highlighting their experience and expertise.
    <br>• Customer or Product Validation: Testimonials, case studies, or early sales data to prove product-market fit.
    <br>• Exit Strategy: Information on potential exit routes (e.g., IPO, acquisition) for the investors.
    </p>                     
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def venturecapitalfaq(request):
    introduction = mark_safe("""
    <p><b><u>FAQs</u></b></p>                        
                             
    <p><b><u>1. What is venture capital?</u></b><br>
    • Answer: Venture capital is a form of private equity financing where investors provide funding to early-stage, high-growth startups in exchange for equity (ownership) in the company.
    </p>
                             
    <p><b><u>2. Who provides venture capital?</u></b><br>
    • Answer: Venture capital is typically provided by VC firms, angel investors, corporate venture arms, or funds backed by institutions or high-net-worth individuals.
    </p>
                             
    <p><b><u>3. At what stage should I seek VC funding?</u></b><br>
    • Answer: Startups typically seek VC funding at the Seed, Series A, or Series B stage—once they’ve validated their product or service and are ready to scale.
    </p>
                             
    <p><b><u>4. How much equity do VCs usually take?</u></b><br>
    • Answer: VCs generally take 10–30% equity in a startup per round, depending on the company’s valuation, market potential, and stage of development.
    </p>
                             
    <p><b><u>5. What do VCs look for in a startup?</u></b><br>
    • Answer: VCs evaluate startups based on team strength, product-market fit, traction, competitive landscape, scalability, and potential return on investment.
    </p>
                             
    <p><b><u>6. How long does it take to raise VC funding?</u></b><br>
    • Answer: It typically takes 3–9 months to raise a VC round, including preparing pitch materials, securing meetings, undergoing due diligence, and finalizing legal agreements.
    </p>
                             
    <p><b><u>7. What documents do I need to present to VCs?</u></b><br>
    • Answer: Common documents include a pitch deck, executive summary, financial model, cap table, business plan (optional), and due diligence materials like customer contracts or product demos.
    </p>
                             
    <p><b><u>8. Do I need to be a C-Corp to raise VC?</u></b><br>
    • Answer: Yes, most VCs require startups to be structured as Delaware C-Corporations for tax, legal, and equity structuring reasons.
    </p>
                             
    <p><b><u>9. What are the risks of VC funding?</u></b><br>
    • Answer: Risks include equity dilution, loss of control, high growth pressure, potential misalignment with investors, and board oversight that may not align with founder vision.</p>
                             
    <p><b><u>10. Do VCs expect a return?</u></b><br>
    • Answer: Yes, VCs invest with the expectation of a 10x+ return over 5–10 years, usually via acquisition or IPO. They typically expect at least one “home run” investment to offset losses from others.
    </p>

    <p><b><u>11. Can I raise VC and still retain control?</u></b><br>
    • Answer: It depends on how much equity you give up and the voting rights attached to VC shares. Founders often retain control in early rounds but may lose majority control in later stages.</p>

    <p><b><u>12. Is venture capital the only way to fund a startup?</u></b><br>
    • Answer: No. Alternatives include bootstrapping, angel investment, grants, crowdfunding, small business loans, and revenue-based financing.</p>                                            
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def venturecapitaltwelve(request):
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
    
    #Up front Cost options
    up_front_cost_options ={
        'Minimum $0 - Maximum $499' : 'Additional funding will be necessary to secure specialized legal counsel with venture capital expertise to oversee term sheet negotiations, capitalization table modeling, and regulatory compliance.',
        'Minimum $500 - Maximum $999' : 'Additional funding will be necessary to secure specialized legal counsel with venture capital expertise to oversee term sheet negotiations, capitalization table modeling, and regulatory compliance.',
        'Minimum $1000 - Maximum $2499' : 'Additional funding will be necessary to secure specialized legal counsel with venture capital expertise to oversee term sheet negotiations, capitalization table modeling, and regulatory compliance.',
        'Minimum $2500 - Maximum $4999' : 'Additional funding will be necessary to secure specialized legal counsel with venture capital expertise to oversee term sheet negotiations, capitalization table modeling, and regulatory compliance.',
        'Minimum $5000 - Maximum $9999' : 'Additional funding will be necessary to secure specialized legal counsel with venture capital expertise to oversee term sheet negotiations, capitalization table modeling, and regulatory compliance.',
        'Minimum $10000 - Maximum $24999' : 'The engagement of experienced venture capital counsel is essential to oversee term sheet negotiations, capitalization table management, and regulatory compliance.',
        'Minimum $25000 - Maximum $49999' : 'The engagement of experienced venture capital counsel is essential to oversee term sheet negotiations, capitalization table management, and regulatory compliance.',
        'More than $50000+' : 'The company must engage qualified venture capital counsel to handle term sheet negotiations, capitalization table management, and ongoing compliance matters.',             
    }
    costanalysis = up_front_cost_options[upfrontcost]

    #Up front Cost options
    up_front_time_options ={
        '1 Day to 1 Week' : 'Your projected timeline of 1 day to 1 week may prove insufficient to fully complete the process, given the complexity of required due diligence and regulatory considerations.',
        '1 Week to 2 Week' : 'Your projected timeline of 1 week to 2 weeks may prove insufficient to fully complete the process, given the complexity of required due diligence and regulatory considerations.',
        '2 Weeks to 4 Weeks' : 'Your projected timeline of 2 weeks to 4 weeks may prove insufficient to fully complete the process, given the complexity of required due diligence and regulatory considerations.',
        '1 Month to 2 Months' : 'Your projected timeline of 1 month to 2 months may prove insufficient to fully complete the process, given the complexity of required due diligence and regulatory considerations.',
        '2 Months to 3 Months' : 'Your projected timeline of 2 months to 3 months may prove insufficient to fully complete the process, given the complexity of required due diligence and regulatory considerations.',
        '3 Months to 6 Months' : 'The estimated 3-6 month timeframe is consistent with typical venture capital fundraising cycles, accounting for investor due diligence, term sheet negotiations, and closing procedures.',
        '6 Months to 12 Months' : 'The projected 6-12 month timeframe represents a viable window for completing a venture capital raise, accounting for comprehensive investor outreach, due diligence, and closing processes.',
        'More than 1 year' : 'The estimated time of more than 1 year timeframe falls within the conventional range for completing a venture capital fundraising round, accounting for investor sourcing, due diligence, and transaction closing.',             
    }
    timeanalysis = up_front_time_options[upfronttime]

    premarketStr = ''
    for num,item in enumerate(premarket):
        if num == 0:
            premarketStr = premarketStr + str(item).lower()
        elif num == (len(premarket)-1):
                premarketStr = premarketStr +', and ' + str(item).lower()
        else:        
            premarketStr = premarketStr +', ' + str(item).lower()    

    introduction = """
    <p><b><u>FINFIRE CAPITAL MATCH REPORT FOR:</b></u><br>
    Venture Capital</p>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
    As {n} enters a {stage} stage, venture capital offers a powerful path to scale rapidly. Unlike angel investment or SAFEs, venture capital typically comes with a formal valuation, structured equity terms, and board oversight. VC is most appropriate for companies with early traction and large-scale growth potential, particularly in markets that offer outsized return opportunities. This makes VC an ideal fit for <b>{n}</b> if it is preparing to aggressively expand.
    </p>
    
    <p><b><u>2 - Entity Type Assessment</b></u><br>
    Venture capital investment is best suited for {entity}, which allow for preferred stock issuance, option pools, and a structured cap table—all standard in VC deals. If {n} is structured as a {entity}, it is well-positioned to receive institutional venture backing. LLCs and S Corps typically need to convert to a C Corp to accommodate VC investment requirements.
    </p>
    
    <p><b><u>3 - Pre Capital Assessment</b></u><br>
    With {preraise} in pre-capital, {n} has demonstrated initial investor confidence and product-market validation. This track record enhances its appeal to venture capitalists, who look for companies that have de-risked early development and are ready to scale. VC firms will now expect data-driven evidence of growth, such as revenue metrics, customer acquisition costs, and engagement KPIs.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
    The shift from early-stage capital to venture capital suggests {n} is maturing into a growth-stage startup. VC investors favor companies that can dominate large markets and achieve exponential returns. With prior funding and a proven concept, {n} is now in a position to engage firms that offer more than capital—such as mentorship, strategic partnerships, and follow-on funding capabilities. 
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
    Raising {raisegoal} through VC will require a clearly defined valuation, a comprehensive investor pitch, and a strong growth narrative. Venture capital rounds—such as Seed, Series A, or Series B—are well-suited for companies like {n} that plan to deploy significant capital across product development, talent acquisition, and market expansion. Investors will expect a detailed use-of-funds and ROI timeline.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
    Venture capital is most common in Seed through Series C rounds. {n}’s place in this trajectory will depend on its traction, revenue stage, and capital needs. For instance, a Series A round often targets product-market fit and initial scaling, while Series B and C rounds emphasize national or global expansion. VCs at each stage assess risk, scalability, and market timing.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
    Venture capital deals may include tranche structures linked to performance milestones (e.g., revenue targets, user growth, or product rollouts). This phased funding approach allows {n} to prove execution capability while minimizing dilution. It also aligns investor confidence with company progress.
    </p>
    
    <p><b><u>8 - Use of Funds Assessment</b></u><br>
    Venture capital funds are typically allocated to:
    <br>- Product development and engineering
    <br>- Customer acquisition and marketing
    <br>- Sales team expansion
    <br>- Operational infrastructure
    <br>- Market entry or expansion
    <br>VCs expect every dollar to drive scalable growth, and will monitor burn rate, runway, and ROI metrics closely.
    </p>
    
    <p><b><u>9 - Risk Assessment</b></u><br>
    Venture capital investors understand high risk and expect high reward. {n} must show credible traction, a strong team, and defensible competitive advantages. While VCs are comfortable with risk, they do perform thorough diligence and will often take board seats or other control rights to mitigate downside.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
    The cost of VC capital is equity dilution and potential loss of full autonomy. VCs seek significant equity stakes and expect 10x returns or more. While there are no interest payments, founders must prepare for intensive reporting, milestone pressure, and eventual exit planning (IPO or acquisition).
    </p>
    
    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
    VC deals incur legal and financial due diligence costs, typically ranging from $25,000 to $150,000, depending on round size and complexity. If {n} has a {upfrontcost} for these services, {costanalysis}
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
    Venture capital fundraising typically takes 2–6 months from initial outreach to closing, though this can vary based on round size and company traction. {n} can reduce this timeline with an investor-ready data room, compelling deck, and strong intros to target VC firms. {timeanalysis}</p>
        """

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime,costanalysis=costanalysis,timeanalysis=timeanalysis))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)