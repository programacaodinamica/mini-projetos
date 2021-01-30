### A Pluto.jl notebook ###
# v0.12.18

using Markdown
using InteractiveUtils

# ╔═╡ e72874ee-6260-11eb-02c7-215be0e4adb6
begin
	using Images, FileIO
	using VideoIO
end

# ╔═╡ fd5f0834-6262-11eb-00de-afcc2e276cbc
img = load("data/testchromakey.jpg")

# ╔═╡ 1fce9d7a-6264-11eb-0ea5-c9305c89ae8b
function greenmask(img)
	hsvimg = HSV.(img)
	channels = channelview(hsvimg)
	hue = channels[1, :, :]
	sat = channels[2, :, :]
	val = channels[3, :, :]
	mask::AbstractArray{N0f8} = ones(size(hsvimg))
	for index in eachindex(hsvimg)
		if 60 ≤ hue[index] ≤ 140 && sat[index] ≥ 30/255 && val[index] ≥ 30/255 
			mask[index] = 0
		end
	end
	mask
end

# ╔═╡ ab3b7c56-6265-11eb-30ac-7f86a2183ee7
begin
mask = greenmask(img)
hcat(img, img .* mask)
end

# ╔═╡ 6f5d1d28-6267-11eb-2ba6-07f6d7bc8bf4
background = imresize(load("data/jp-1080p.jpg"), size(img))

# ╔═╡ 7ba2eb9e-6267-11eb-2b18-8195f28580b0
begin
	invmask::AbstractArray{N0f8} = ones(size(mask)) - mask
	hcat(background, invmask .* background)
end

# ╔═╡ 25925a54-6268-11eb-2df1-e189c8a5f634
function changebg(img, bg, mask)
	invmask::AbstractArray{N0f8} = ones(size(mask)) - mask
	invmask .* bg + mask .* img	
end

# ╔═╡ 52607d3a-6269-11eb-1cb6-d13b05ce67c8
changebg(img, background, mask)

# ╔═╡ e8c1f786-6269-11eb-0d01-63f9223b2769
function changevideobg(inputdir, bgdir, outputdir)
	worksize = (1080, 1920)
	video = VideoIO.openvideo(inputdir)
	bg = RGB.(imresize(load(bgdir), worksize))
	frames = []
	for frame in video
		img = imresize(frame, worksize)
		push!(frames, changebg(img, bg, greenmask(img)))
	end
	props = [:priv_data => ("crf"=>"22","preset"=>"medium")]
	encodevideo(outputdir, frames, framerate=30, AVCodecContextProperties=props)
end

# ╔═╡ 55617cac-626a-11eb-0e8b-1b52846a7c03
changevideobg("data/meuchromakey.mov", "data/jp-1080p.jpg", "output/bgjptest.mov")
# changevideobg("data/pteste.mp4", "data/veleiro.jpg", "output/bgjp.mov")

# ╔═╡ Cell order:
# ╠═e72874ee-6260-11eb-02c7-215be0e4adb6
# ╠═fd5f0834-6262-11eb-00de-afcc2e276cbc
# ╠═1fce9d7a-6264-11eb-0ea5-c9305c89ae8b
# ╠═ab3b7c56-6265-11eb-30ac-7f86a2183ee7
# ╠═6f5d1d28-6267-11eb-2ba6-07f6d7bc8bf4
# ╠═7ba2eb9e-6267-11eb-2b18-8195f28580b0
# ╠═25925a54-6268-11eb-2df1-e189c8a5f634
# ╠═52607d3a-6269-11eb-1cb6-d13b05ce67c8
# ╠═e8c1f786-6269-11eb-0d01-63f9223b2769
# ╠═55617cac-626a-11eb-0e8b-1b52846a7c03
