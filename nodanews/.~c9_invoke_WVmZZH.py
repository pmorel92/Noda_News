from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.template import Context
from django.template.defaulttags import register
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Q
from .models import Blog, Event, Theme, Report_Link, Node, Media_Org, Perspective, Link, Node_Dir, Region, Journalist, About, Topic_Link, PoliticalBiasNews, Blog, Analysis, AnalLink, AnalPerspective, PoliticalIssue, STF, STF_Hub, STF_Link, Feature, Feature_Link

def index(request):
	return render (request, 'index.html')

def indexUC(request):
    
    return render (request, 'indexUC.html')

def blog(request, slug, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog.html', {'blog': blog})


############Archives#################

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def political_issue(request, slug, issue_id):
    issue = get_object_or_404(PoliticalIssue, pk=issue_id)
    issue_links = PoliticalBiasNews.objects.filter(issue__id = issue_id).order_by('-posted')
    return render(request, 'Archives/issue.html', {'issue': issue, 'issue_links': issue_links})

def about(request):
    abouts = About.objects.all()
    return render(request, 'Archives/about.html', {'abouts': abouts})

def node_dir(request):
    node_dir_topics = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    node_dirs = Node_Dir.objects.order_by('name')
    nodes_by_dir = {
        n: Node.objects.filter(node_direc__id = n.id).order_by('-date_posted')[0:3] for n in node_dirs
    }
    return render(request, 'Archives/node-dir.html', {'node_dirs': node_dirs, 'nodes_by_dir': nodes_by_dir, 'node_dir_topics': node_dir_topics})

def node_dir_part(request, node_dir_id , slug):
    node_dir = get_object_or_404(Node_Dir, pk=node_dir_id)
    nodes = Node.objects.filter(node_direc__id = node_dir_id)
    stfs = STF.objects.filter(node_dir__id = node_dir_id)
    return render(request, 'Archives/node-dir_part.html', {'nodes': nodes, 'node_dir': node_dir, 'stfs': stfs})	

def media_dir_athena(request):
	medias = Media_Org.objects.all()
	return render(request, 'Archives/media-org-directory.html', {'medias': medias})

def archives(request):
    node_dirs = Node_Dir.objects.order_by('name')
    blogs = Blog.objects.all().order_by("-date_posted")
    indepths = Analysis.objects.all().order_by("-date_posted")
    issues = PoliticalIssue.objects.all().order_by("-id")
    nodes_by_dir = {
        n: Node.objects.filter(node_direc__id = n.id).order_by('-date_posted') for n in node_dirs
    }    
    return render(request, 'Archives/archives.html', {'node_dirs': node_dirs, 'blogs': blogs, 'indepths': indepths, 'issues': issues, 'nodes_by_dir': nodes_by_dir})



def node(request, node_id):
    node = get_object_or_404(Node, pk=node_id)
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    assnodes = Node.objects.filter( node_direc__id = node.node_direc_id)
    perspectives = Perspective.objects.filter( node__id = node_id )
    perspective_links = {
		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'Archives/node.html', {'node': node, 'perspectives': perspective_links, 'node_dirs': node_dirs, 'assnodes': assnodes})

def nodeslug(request, slug, node_id):
    node = get_object_or_404(Node, pk=node_id)
    node_dirs = Node_Dir.objects.filter(active=True).order_by('-date_updated')
    assnodes = Node.objects.filter( node_direc__id = node.node_direc_id)
    perspectives = Perspective.objects.filter( node__id = node_id )
    perspective_links = {
		p: Link.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'Archives/node.html', {'node': node, 'perspectives': perspective_links, 'node_dirs': node_dirs, 'assnodes': assnodes})

def stf_hub(request, slug, stf_hub_id):
	stf_hub = get_object_or_404(STF_Hub, pk=stf_hub_id)
	stfs = STF.objects.filter( hub__id = stf_hub_id)[0:7]
	stf_links = {
		p: STF_Link.objects.filter(story__id = p.id) for p in stfs
	}	
	return render(request, 'Archives/hub.html', {'stf_hub': stf_hub, 'stfs': stf_links})

def stf_hubx(request, slug, stf_hub_id):
	stf_hub = get_object_or_404(STF_Hub, pk=stf_hub_id)
	stfs = STF.objects.filter( hub__id = stf_hub_id)
	stf_links = {
		p: STF_Link.objects.filter(story__id = p.id) for p in stfs
	}	
	return render(request, 'Archives/hubx.html', {'stf_hub': stf_hub, 'stfs': stf_links})	

def stf(request, slug, stf_id):
	stf = get_object_or_404(STF, pk=stf_id)
	stf_links = STF_Link.objects.filter( story__id = stf_id)
	return render(request, 'Archives/story.html', {'stf': stf, 'stf_links': stf_links})
	
def analysis(request, slug, analysis_id):
    analysis = get_object_or_404(Analysis, pk=analysis_id)
    perspectives = AnalPerspective.objects.filter( article__id = analysis_id )
    perspective_links = {
		p: AnalLink.objects.filter(perspective__id = p.id) for p in perspectives
	}
    return render(request, 'Archives/in-depth.html', {'analysis': analysis, 'perspectives': perspective_links})
    

def media_org(request, slug, media_org_id):
    media_org = get_object_or_404(Media_Org, pk=media_org_id)
    journalists = Journalist.objects.filter( organization__id = media_org_id )
    return render(request, 'Archives/media_org.html', {'media_org': media_org, 'journalists': journalists,})	

def journalist(request, slug, journalist_id):
	journalist = get_object_or_404(Journalist, pk=journalist_id)
	return render(request, 'Archives/journalist.html', {'journalist': journalist})
	
	